import torch

# 创建线性的张量 创建随机的张量

t1=torch.arange(1,20,2)
print(t1)
print("-" * 54)
#  等差数列 一共5个数 全包含
t2=torch.linspace(1,20,5)
print(t2)
print("-" * 54)


torch.manual_seed(1)

# 符合正态分布的随机张量
t3=torch.randn(size=(3,4),dtype=torch.float16)
print(t3)
print("-" * 54)

#符合0，1分布的随机张量

t4=torch.rand(size=(3,4))
print(t4)
print("-" * 54)

# 随机整数的随机张量
t6=torch.tensor([1,3,4,5],dtype=torch.int32)  #int32
print(t6)
t7=t6.type(torch.float16)   # 通用写法

#   各元素数据类型的转换


#   long  short int  half float double

print(t6.half())  # float16
print(t6.double)  # float64
print(t6.int())       #int32
print(t6.float())
print(t6.short())
print(t6.long())  #int64默认
