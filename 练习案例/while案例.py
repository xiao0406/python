# 需求:通过while循环，计算从1累加到100的和
# 提示:
# 1.终止条件不要忘记，设置为确保while循环100次
# 2.确保累加的数字，从1开始，到100结束

i = 1
count = 0;
while i<=100:
    count +=i+1
    i += 1
print(count)





# 需求：猜随机数
# 生成10以内的随机数
count = 0
flag = True
import random
num = random.randint(1,10)
while flag:
    count +=1
    num1= int (input("请输入一个10以内的随机数:"))
    if num == num1:
        print(f"恭喜您猜中了,结果是{num1}")
        print(f"随机数是{num}")
        flag = False
    else:
        if num1 > num:
            print("猜大了")
        else:
            print("猜小了")
print(f"您猜了{count}次")