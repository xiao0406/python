'''
for 临时变量 in 待处理数据集(可迭代对象):
        循环满足条件时执行的代码
从待处理数据集中：逐个取出数据赋值给临时变量
'''

# name = "hello"
# for x in name:
#     print(x)

# abcddgasgafafdsf 有几个a出现
# name = "abcddgasgafafdsf"
# count = 0
# for e in name:
#     if 'a' == e :
#         count += 1
# print(count)


# a = [1,1.1,"2,2"]
# for e in a:
#     print(f"类型是：{type(e)}，结果是：{e}")

# range语法
'''
语法一: range(num)
获取一个从0开始，到num结束的数字序列（不含num本身）,如range(5)取得的数据是：[0, 1, 2, 3, 4]
'''
# for x in range(5):
#     print(x)

'''
语法二: range(num1，num2)
获得一个从num1开始，到num2结束的数字序列（不含num2本身）
如，range(5, 10)取得的数据是：[5, 6, 7, 8, 9]
'''
# for x in range(5, 10):
#     print(x)

'''
语法三: range(num1, num2, step)
获得一个从num1开始，到num2结束的数字序列（不含num2本身）
数字之间的步长(相当于间隔数)，以step为准（step默认为1）
如，range(5, 10, 2)取得的数据是：[5, 7, 9]
'''
# for x in range(5,10,3):
#     print(x)


# 定义一组数，求偶数出现的个数
# count = 0
# for x in range(1,100):
#     if x %2 == 0:
#         count += 1
# print(count)

'''
break 和continue关键字
break推出循环
continue 退出本次循环
'''
# for i in range(1,9):
#     if i == 3:
#         continue
#     print(i)

# for i in range(1,9):
#     if i == 3:
#         break
#     print(i)




