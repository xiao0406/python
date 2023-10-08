# end = '' 可以做到不换行
# print("hello",end='')
# print("World",end='')

# \t 等同于键盘按下tab
# print("abcd")
# print("abcdef")
# print("ab\tcd")
# print("abc\tdef")

# 案例：通过while打印出九九乘法表
# 1*1 = 1
# 1*2 = 2 2*2 = 4

i = 1
while i<=9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j*i}\t",end='')
        j +=1
    i +=1
    print()


