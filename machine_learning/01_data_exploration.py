"""Kaggle Intro to Machine Learning 第 1 课：数据探索。

读入墨尔本房价数据，用 .describe() 看每一列的整体统计。
"""
from sklearn.tree import DecisionTreeRegressor
from pathlib import Path

import pandas as pd

# __file__ 是当前脚本的路径，向上两级就是项目根目录，再进 data/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "melb_data.csv"

if not DATA_FILE.exists():
    raise SystemExit(f"找不到数据文件：{DATA_FILE}\n请按 data/README.md 的说明下载 melb_data.csv")

dataset = pd.read_csv(DATA_FILE)
print(dataset.describe())
print(dataset.columns)
melbourne_data = dataset.dropna(axis=0)
print(melbourne_data.head())
"""
  dropna 的方法返回的是一个新的列表 之前的列表不变  axis=0 是对应的行 
  tail是输出表格的后几行 默认值是5行
  head是输出表格的前几行 默认值是5行
  columns方法是查看所有的列名 返回的是一个index对象
  创建决策树模型 引入库
  自动拟合模型 不用有返回值接收 直接修改原模型对象
  然后模型对象用用特征预测房价
  这个随机种子是干嘛的？
  
  
"""
y = melbourne_data.Price #    访问的是一列
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
print(X.head())
melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(X, y)
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))





