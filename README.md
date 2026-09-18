# Python AI 学习

记录我的 Python、机器学习、深度学习和人工智能学习过程。

## 学习路线

Python 基础 → 数据分析 → 机器学习 → 深度学习 → AI 应用开发

## 目录结构

```
Python-Learning/
├── data/                 所有练习共用的数据集（不进 Git）
├── docs/                 学习笔记
│   ├── python_basics.md
│   ├── heima_notes.md
│   └── deep_learning.md
├── python_basics/        Python 基础语法练习
│   ├── 01_basic_syntax.py
│   ├── 02_containers_and_oop.py
│   ├── 03_scratch.py
│   └── mypackage/        自定义包练习（__init__.py + 模块）
├── machine_learning/     机器学习
│   └── 01_data_exploration.py
├── deep_learning/        深度学习（PyTorch）
│   ├── 01_tensor_creation.py
│   ├── 02_tensor_random_and_dtype.py
│   ├── 03_dataset_and_dataloader.py
│   ├── 04_tensor_operations.py
│   └── check_env.py      环境自检（显卡 / CUDA / 精度对比）
├── leetcode/             算法练习
└── outputs/              代码生成的文件（图表、模型等，不进 Git）
```

命名约定：脚本统一用「序号_内容」的形式，序号就是学习顺序。

## 环境

- Python 3.14，CUDA 版 PyTorch
- 依赖清单见 `requirements.txt`

```
pip install -r requirements.txt
```

## 怎么运行

PyCharm 里右键脚本 → Run 就行。脚本内部用「相对本文件」的方式定位数据
（见 `machine_learning/01_data_exploration.py`），所以 PyCharm 的工作目录设成什么
都不会出现找不到文件的问题。

## PyCharm 设置

`.idea/` 里的 IDE 配置不进 Git（换电脑时 PyCharm 会自己重建），所以新环境里要手动做一次：

- 右键 `data/` 和 `outputs/` → Mark Directory as → Excluded，这两个目录不用建索引
- 解释器选本机装好 torch 的那个 Python 3.14

## 学习记录

已完成：

- [x] GitHub 环境搭建
- [x] PyCharm 配置
- [x] Python 基础语法（黑马程序员课程）
- [x] PyTorch 张量基础、Dataset / DataLoader
- [x] Kaggle Intro to Machine Learning 第 1 课：数据探索
