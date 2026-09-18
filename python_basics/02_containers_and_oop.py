print('a')
set_1={"A","1","31"}
set_1.add("B")

print(set_1)

print("\n")

print(f"比较的大小内容是{sorted(set_1,reverse=True)}")

#f=open("D:/test.txt","a",encoding="utf-8")     #a方法和w方法的不同和注意事项
#.write("学python来黑马程序员")
#f.write("666")
#f.close()


#  创建一个返回函数令他的返回值为对象或者另一个函数

#  创建一个类对象 完成继承 多态的实现  魔术方法的使用 私有变量 私有方法

#  创建一个包 引入包 包的特征 利用包里面的全局变量导入了模块

# 包练习：mypackage 是 python_basics 下的自定义包（原 practice 包）
from mypackage import *

hackerrank_weird.re()

stu=[1,2,5,9,"ab",{"stud":{"stud2":2}}]
print(stu[5]["stud"]["stud2"])
#print(sorted(stu))
#print(max(stu))
#print(min(stu))
str_= "AB CDEFG"
ST=str_.replace("A","B")
print(ST[1])
print(str_)
a = int(input())
b = int(input())
print(f"整数除法的结果{a // b}")
class Student:
    def bark(self):
        pass
class Student_1:
    def bark(self):
        print("郭佳怡喵喵叫")
class Student_2:
    def bark(self):
        print("郭佳怡呱呱叫")
Student_1().bark()
Student_2().bark()

