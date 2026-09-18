"""
print("Hello Python!")

name = "JF"

age = 20

print(name)
print(age)

print( type(name))

print( type(age))


tmp=5/3
print(tmp)

tm=5//3
print (tm)


l=5**3
print(l)


m=5.75*2-3

print(m)


s = 'First line.\nSecond line.'  # \n 表示换行符
s  # 不用 print()，特殊字符将包括在字符串中
print(s)  # 用 print()，特殊字符会被转写，因此 \n 将产生一个新行
print( ' NIHAO'  )
print('你好')
print("你好")
t="\"Yes,\" they said."
t="doesn't"

print(t)

' doe sn\'t'  # 使用 \' 来转义单引号...

"doesn't"  # ...或者改用双引号

'"Yes," they said.'

"\"Yes,\" they said."

'"Isn\'t," they said.'


print('C:\this\name')  # 这里 \t 表示制表符，\n 表示换行符


print(r"C:\this\nam")  # 请注意引号前的 r



n=[1,3,"HELLO"]

print(n)

f=n[0:2]

print(f)

w=[1,3.14,9]

float3=int(3.1415926)

print(type(float3),float3)

float_3=98799

age=input("请输入信息")
print("你好")

if age <= 18 :
    print("ni hao c heng nian ren")
    print("硕士 你好")
elif age>18:
    print("nih ao che  n gni an r en")



i = 3
while i<10:
    print(i)
    i+=1
    if i<8:
        print("hello")

i = 1
sum = 0
while i<= 100:
    sum += i
    i += 1
print(sum)

for x in range(1,11):
    print(x)
    for x in range(1,10):
        print("语句一")
        break
        print("语句二")
print("语句三")

age = int(input("请输入你的年龄"))

if age >= 18:
    print("你好成年人")
print("玩的开心祝你")


num=None

def ate(a, b):
    num = a + b
    return num

result = ate(a=1, b=3)
print(result)

"""


def ate(a,b):

    num = a + b
    return num
result = ate(a=1, b=4)



n=(1,5,"PYTHON",1)
M=n.index("PYTHON")
print(M)

number=n.count(1)
print(number)

numb=len(n)
print(numb)




lit_1=[1,"python",3,4,1]

ele=lit_1.index(1)
print(ele)

lit_1.append("love")
print(lit_1)

lit_1.extend([1,5])
print(lit_1)

lit_1.pop(1)

print(lit_1)

del lit_1[1]
print(lit_1)

lit_1.remove(1)
print(lit_1)

NUM=lit_1.count(1)
print(NUM)




st="pytho,666,java"
print(f"输出的内容是{st}","类型是{type(st)}")

st2=st.replace("666","A")
print(st2)

lit2=st.split("a")
print(lit2)

st3=st.strip("a")
print(st3)

st4=st2.strip()
print(st4)

NUME=st.count("a")
print(NUME)


st5="HELLO PYTHON"
print(st5)

ST=st5[::-2]

print(ST)

my_dict={"郭佳怡":9999,"焦泓棐":666 }

MUN=my_dict["郭佳怡"]
print(MUN)


MY_dict = {
    "郭佳怡": {"你好": 666},
    "焦泓来": {888}   # 空字典，或者 {"键": 值}
}

muy={"你好":{"NI":66},"哈哈":{"WUWEI":55}
     }

print(muy["你好"]["NI"])

muy["焦"]=int(89)
print(muy)

muy["NIHYAS"]=int(56)
print(muy)

for x in muy:
    print(f"字典通过循环的结果是{x},他们对应的键值是{muy[x]}")

# 数字 小于 小写英文 小于大写英文 ascii值

print(f"比较的结果是{"A"<"a" }")

def retur_1():
    return 1 , 2, 3
x,y,z=retur_1()
print(x)
print(y)
print(z)


def add(a,b):
    l=a+b
    print(f"输出的结果是{l}")
add(1,3)

Lit=[1,3,4,1]
print(Lit)
v=(max(Lit))
print(v)
print(f"比较的结果是{ sorted(Lit) }")

Lit.remove(1)
print(Lit)


del Lit[0]
print(Lit)

ni=Lit.pop(1)
print(Lit)
print(ni)


#lambda

#数据容器类型间的转换  字典的键值会不会消失 在转化为字符串的时候不会


#m=open("D:/test.txt","w",encoding="UTF-8")

#m.write("guojiayishishazi")

#m.close()

set_1={1,"2",3}
set_2={1,"python",5,"2"}
set_3=set_1.difference(set_2)  # 保留差集到一个新的集合
print(set_1)
print(set_2)
print(set_3)

set_1.difference_update(set_2)   #消除差集在原有的集合上进行处理

print(set_1)
print(set_2)

set_3=set_1.union(set_2)
print(set_3)


#try:  #尝试捕获异常  可能出现的bug

#except:  #及时的对bug的处理情况
    #print()




#except Exception as ex:
#print(ex)


import time
print('nihao')
#time.sleep(5)
print("GUO JIAO")
#from time import sleep

#if __name__ =="__main__":
   # print("nihao")

#  数据可视化的模块介绍  pyecharts
"""from pyecharts.charts import Line
line=Line()
line.add_xaxis(["中国","美国","日本"])
line.add_yaxis("GDP",[30,20,90])
line.render()


 json本质上是字符串 可以用字符串的方法去处理他
"""


class Student:  #里面包括类的属性 类的行为(函数)
    name=None
    age=None
    def say_hi(self):
        print(f"你好 我的名字是{self.name}，我的年龄是{self.age}")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("构造成功了")


stu_1=Student("JD","20")

print(stu_1.name)
# print(stu_1) # 格式错误
stu_1.say_hi()

# 类和对象的关系

#类的内置方法, 本质上是私有变量和方法


#继承的引入
class Student2(Student):
   pass

#类型注解  形参  返回值  变量



#  list.append()


# 数据的读取 然后进行数据的分析处理


a=open("D:/test.txt","r",encoding="UTF-8")
#for line in a:
   # print(line)
I=a.read()
print(I)
a.close()








