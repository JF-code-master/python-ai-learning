import torch

import numpy as np

# torch更换为numpy数组  不共享.copy的形式

t1=torch.tensor([[1,2,3],[4,5,6]])

t2=np.array([11,22,33])

t3=t1.numpy()

print(f"t3的内容是 {t3}")

t2[1]=44
print(f"更新前的内容是{t1},类型是{type(t1)}")
print(f"t1更改后的内容是{t1},类型是{type(t1)}")

#更改的是数组里的值 共享内存  共享的概念是什么

t4=torch.from_numpy(t2)

print(f"输出的类型是{type(t4)},输出的内容是{t4}")

t6=torch.tensor([[11,22,33],
                 [4,5,6]
])

t5=t6*t1
print(t5)

print("-" * 66)

#  对 张量 内的元素进行运算


t1.add_(10)
print(t1)

t1.sub_(10)
print(t1)

t1.mul_(2)
print(t1)

#t1.div_(1)
#print(t1)

t1.neg()
print(t1)


print("*"*66)

#  对张量内的元素进行常见运算

# max  min  mean sum  有具体的dim值 按行 或 列 进行运算

# pow exp log  sqrt

t1.max(dim=0) # 0代表lie 1 代表行
print(t1)
print("-"*66)


t1.min(dim=0)
print(t1)
print("-"*66)


t1.sum()
print(t1)
print("-"*66)

t1.float().mean(dim=0)
print(t1)
print("-"*66)

T1=torch.tensor([[1,2,3],[4,5,6]],dtype=torch.float16)
T2=torch.tensor(
 [    [1,2]
    , [4,5]    ,
      [6,7]]   ,
dtype=torch.float16)

T3=T1@T2
print(T3)
print(T3)
print("-"*66)

#   进行索引等操作  简单的行列索引 范围索引 布尔索引 多维索引 引入0维 1维 2维的概念 维度的概念是在计算机中用 [] 表示的吗
torch.manual_seed(1)

t8=torch.randint(1,10,size=(3,4))
print(t8)
print("*"*88)

t9=t8[0,:]
print(t9)

t11=t8[:,0]
print(t11)

t10=t8[[0,1],[2,3]]
print(t10)

#t11=t8[[[0],1],[0,1]]
#print(t11)

t12=t8[:2,3:]
print(t12)

t13=t8[:2,:2]
print(t13)




# 对张量形状做改变  reshape permute  squeeze contiguous transpose  view



w=torch.tensor(10,requires_grad=True,dtype=torch.float16)
print(w)

 # w旧=w新-学习率*梯度

loss=2 *w **2 +30

loss.backward()

w=w.data-0.1*w.grad
print(w)















