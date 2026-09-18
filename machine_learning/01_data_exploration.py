"""Kaggle Intro to Machine Learning 第 1 课：数据探索。

读入墨尔本房价数据，用 .describe() 看每一列的整体统计。
"""

from pathlib import Path

import pandas as pd

# __file__ 是当前脚本的路径，向上两级就是项目根目录，再进 data/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "melb_data.csv"

if not DATA_FILE.exists():
    raise SystemExit(f"找不到数据文件：{DATA_FILE}\n请按 data/README.md 的说明下载 melb_data.csv")

dataset = pd.read_csv(DATA_FILE)
print(dataset.describe())
