def re():
    print("我是方法一的函数")
#    re()
if __name__ == '__main__':  # 不能有返回值？ 用exit 推出程序

    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    #if n < 1 or n > 100:
           # return False
    elif n % 2 == 0:
        if  2 <= n <= 5 :
             print("Not,Weird")
        elif 6<= n <= 20 :
            print("Weird")
        elif n>20:
             print("Not，Weird")

