import torch
from torch.utils.data import TensorDataset, DataLoader
from sklearn.datasets import make_regression

def create_set():
    x, y, coef = make_regression(
        n_samples=100,
        n_features=1,
        noise=10,
        random_state=0,
        coef=True,
    )
    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)
    return x, y, coef

x, y, coef = create_set()
print(x.shape, y.shape, coef)      # torch.Size([100, 1]) torch.Size([100]) 系数

dataset = TensorDataset(x, y)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

for batch_x, batch_y in dataloader:
    print(batch_x.shape, batch_y.shape)

