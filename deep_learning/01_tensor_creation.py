import torch



t1=torch.ones(3,4)    #  创建的是三行四列的全1张量
print(f"打印的内容是{t1},类型是{type(t1)}")
print("-"*30)


t2=torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
print(f"打印输出的内容是{t2},类型是{type(t2)}")
print("-"*30)

t3=torch.ones_like(t2)
print(f"打印输出的内容是{t3},类型是{type(t3)}")
print("*"*30)


t4=torch.zeros(2,3)
print(f"打印输出的内容是{t4},类型是{type(t4)}")
print("-"*30)

t5=torch.tensor([[1,2],[4,5],[7,8]])
print(f"打印输出的内容是{t5},类型是{type(t5)}")
print("-"*30)

t6=torch.zeros_like(t5)
print(f"打印输出的内容是{t6},类型是{type(t6)}")
print("-"*30)
print("*"*30)


t7=torch.full(size=(3,4),fill_value=166 )
print(f"打印输出的内容是{t7},类型是{type(t7)}")
print("-"*30)


t8=torch.tensor([[1,2],[4,5],[7,9]])
print(f"打印输出的内容是{t8},类型是{type(t8)}")
print("-"*30)


t9=torch.full_like(t8,199)
print(f"打印输出的内容是{t9},类型是{type(t9)}")
print("-"*30)


# tensor 方法创建指定类型的张量  一维  二维列表 三维的 等等等
#Tensor 方法 与 tensor方法的不同
# tensor数据的几种类型

t10=torch.FloatTensor(10)
print(f"输出的结果是{type(t10)},{t10}")
t11=torch.IntTensor(10)




























