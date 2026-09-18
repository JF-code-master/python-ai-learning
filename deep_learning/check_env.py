"""深度学习环境自检脚本

用法：
    python check_env.py

依次检查：
1. Python / PyTorch / CUDA / cuDNN 版本
2. 显卡型号、显存、算力、bf16 支持
3. 当前 PyTorch 是否为本卡算力（sm_xx）编译过内核
4. 在显卡上实算矩阵乘法，确认数据真的能上卡
5. 对比 fp32 / fp16 / bf16 三种精度的速度，看 Tensor Core 能快多少

注意：第一个 CUDA 运算会包含 cuBLAS 加载和选算法的开销，明显偏慢是正常的，
所以下面每次都先预热再计时。
"""

import platform
import sys
import time

import torch


# 各 CUDA 通道需要的显卡驱动下限（NVIDIA CUDA 版本说明）
DRIVER_HINT = (
    "  - CUDA 12.6 / 12.8：驱动 >= 525（12.8 建议 >= 570）\n"
    "  - CUDA 12.9：驱动 >= 575\n"
    "  - CUDA 13.0（cu130）：驱动 >= 580（R580）\n"
    "  - CUDA 13.2（cu132）：驱动 >= 595（R595）\n"
    "  先运行 nvidia-smi，看右上角 CUDA Version，再选通道。"
)

DTYPES = [
    ("fp32", torch.float32),
    ("fp16", torch.float16),
    ("bf16", torch.bfloat16),
]


def check_arch() -> bool:
    """检查当前 PyTorch 是否为本卡算力编译过内核。"""
    major, minor = torch.cuda.get_device_capability(0)
    sm = f"sm_{major}{minor}"
    arch_list = torch.cuda.get_arch_list()
    print("本卡算力标签 :", sm)
    print("本包已编译支持:", arch_list)
    if sm not in arch_list:
        print(f"问题：当前 PyTorch 没有为 {sm} 编译内核，运算会直接报错。")
        print("解决办法：换成包含该架构的 CUDA 通道重装，例如")
        print("  pip uninstall -y torch torchvision")
        print("  pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130")
        print(DRIVER_HINT)
        return False
    return True


def matmul_time(n: int, dtype: torch.dtype, warmup: int = 3, runs: int = 5) -> tuple[float, float]:
    """返回 (首次调用耗时, 预热后中位耗时)，单位秒。"""
    a = torch.randn(n, n, device="cuda", dtype=dtype)
    b = torch.randn(n, n, device="cuda", dtype=dtype)
    torch.cuda.synchronize()

    t0 = time.perf_counter()
    torch.matmul(a, b)
    torch.cuda.synchronize()
    first = time.perf_counter() - t0

    for _ in range(warmup):
        torch.matmul(a, b)
    torch.cuda.synchronize()

    times = []
    for _ in range(runs):
        t0 = time.perf_counter()
        torch.matmul(a, b)
        torch.cuda.synchronize()
        times.append(time.perf_counter() - t0)
    times.sort()

    del a, b
    torch.cuda.empty_cache()
    return first, times[len(times) // 2]


def benchmark(n: int = 4096) -> None:
    flops = 2 * n**3
    results = {}
    print(f"矩阵乘法规模    : {n} x {n}（每次先预热 3 遍，再取 5 次中位数）")
    for name, dtype in DTYPES:
        first, median = matmul_time(n, dtype)
        results[name] = median
        print(
            f"  {name}: 首次 {first * 1000:7.1f} ms | 稳定 {median * 1000:7.2f} ms "
            f"| {flops / median / 1e12:6.2f} TFLOPS"
        )

    base = results["fp32"]
    print("-" * 54)
    print(f"fp16 相对 fp32 提速: {base / results['fp16']:.1f} 倍")
    print(f"bf16 相对 fp32 提速: {base / results['bf16']:.1f} 倍")
    print("（fp16/bf16 走 Tensor Core，训练时开混合精度就是靠这个加速）")


def main() -> None:
    print("=" * 54)
    print("Python       :", sys.version.split()[0], "|", platform.platform())
    print("PyTorch      :", torch.__version__)
    print("CUDA 编译版本 :", torch.version.cuda)
    print("cuDNN        :", torch.backends.cudnn.version())
    print("-" * 54)

    if not torch.cuda.is_available():
        print("CUDA 不可用。两种常见原因：")
        print("  1) 装成了 CPU 版（Windows 上直接 pip install torch 就是 CPU 版）")
        print("  2) 驱动版本低于该 CUDA 通道的要求，报 cudaErrorInsufficientDriver")
        print("先运行 nvidia-smi，看右上角 CUDA Version：")
        print(DRIVER_HINT)
        print("参考 https://pytorch.org/get-started/locally/ 重新安装对应通道。")
        return

    print("可用显卡数   :", torch.cuda.device_count())
    print("显卡型号     :", torch.cuda.get_device_name(0))
    props = torch.cuda.get_device_properties(0)
    print("显存         :", round(props.total_memory / 1024**3, 1), "GB")
    print("算力 SM      :", torch.cuda.get_device_capability(0))
    print("支持 bf16    :", torch.cuda.is_bf16_supported())
    print("-" * 54)

    if not check_arch():
        return
    print("-" * 54)

    try:
        benchmark()
    except RuntimeError as exc:
        print("GPU 运算失败:", exc)
        print("提示：多半是装了不含本卡算力内核的版本，换通道重装。")
        return

    print("-" * 54)
    print("环境正常，可以开始动手了。")


if __name__ == "__main__":
    main()
