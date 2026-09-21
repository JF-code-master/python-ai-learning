from tokenize import PlainToken

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

#  如何构造numpy数组 直接创建 线性的 随机的 线代的 特殊的

np_9=np.arange(1,10,2,dtype=int)
print(np_9)

np_1=np.linspace(1,20,4,dtype=int)
print(np_1)

np_2=np.random.rand(2,3)  #0到1的均匀分布浮点数
print(np_2)

np_3=np.random.randn(2,3)
print(np_3)

np_4=np.random.uniform(1,20,(2,3))
print(np_4)

print(np_4.shape)


N=np.copy(np_4)
print(N)

print(N.ndim)
print(N.dtype)


np_5=np.zeros((2,3))
print(np_5)

np_6=np.diag([1,2,3,4])
print(np_6)

np_7=np.zeros_like(np_6)
print(np_7)

np_8=np.empty((2,3)) #  和zeros有什么不同  为什么是全空数组
print(np_8)

np_9=np.logspace(1,3,5)   #logspace
print(np_9)

#  访问series里的属性  有

np_=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int)
print( np_ * 3)

np.median(np_)
print(np_)




bo=pd.Series([1,2,3,4,5,6],index=["a","b","c","d","e","f"],dtype=int)

#  熟悉series的方法

print(bo)
print(bo.size)
print(bo.index)
print(bo.head())
print(bo.tail())
print(np_.shape)
print(bo.mean())
print(bo.loc['a':'c'])
print(bo.isna().count())

bo_=pd.Series(bo,index=["a","b","c"],dtype=int)
print(bo_)

Bo=pd.Series({0:'n',1:'I'})
print(Bo)


BO=pd.DataFrame({0:bo,1:Bo},index=["a","b"])
print(BO)






"""

numpy数组的比较函数 与0维的 与1维的  
numpy数组的索引与切片 冒号逻辑 逗号逻辑 布尔逻辑 

"""


print(np.greater(np_,2)) # 为什么不能直接用数组名和.的方法
print(np.equal(np_,2))
print(np.less(np_,2))

print(np_[2])



#  print(np_[:,np_>2]) #布尔？ 全覆盖  单取列
#  print(np_[:,[np_>2]])  # 有什么不同






















"""

plt.figure(figsize=(5,3))
plt.plot(["焦","泓","棐"],[1,2,3],label="焦泓棐",color='orange',linestyle="--",alpha=0.5)
plt.title("焦鸿飞大全",fontsize=20)
plt.legend(loc="upper left",fontsize=10))
plt.grid(True,axis="y",alpha=0.3)
plt.show()
plt.ylim(1,100)
plt.tight_layout()



#  如何优化他们

plt.figure(figsize=(5,4))
x=np.random.randint(1,10,10)
y=np.random.randint(1,20,10)

plt.scatter(x,y,color="red",label='焦泓棐',s=50,alpha=0.5)
plt.xlabel('他说你好',fontsize=15)  #转变角度的是什么参数 rotation
plt.ylabel('你说他好',fontsize=15)
plt.legend(loc="upper left",fontsize=10)
plt.title('你好之家',fontsize=20)
plt.grid(True,alpha=0.3,linestyle="-",color='black')
plt.tight_layout()
plt.plot(x,y)
plt.show()

plt.bar(['语文','数学','英语'],[96,97,100],color='red',label='最棒的',alpha=0.5)

plt.xlabel('牛逼',fontsize=15)
plt.ylabel('低调',fontsize=15)

plt.title('跪下',fontsize=20)
plt.grid(True,axis= 'y',alpha=0.3,linestyle="-",color='red')
plt.tight_layout()
plt.show()

plt.pie([1,3,4,5,9],labels=['你好','不好','很好','很不好','超棒的'],autopct='%.1f%%',startangle=90,wedgeprops={'width':0.5})

plt.title('幸福之家',fontsize=20)
plt.tight_layout()
plt.show()


"""