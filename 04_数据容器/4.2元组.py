'''
元组同列表一样,但一旦定义完成，就不可修改

基本格式：
# 定义元组
变量名称 = (元素1, 元素2, 元素3, 元素4, 元素5)
# 定义只有一个元素的元组,需要后面加“，”
变量名称 = (元素1,)
# 定义空元组
变量名称 = ()
变量名称 = tuple()
'''

my_tuple1 = ("张三",18)
my_tuple2 = ("李四",)
my_tuple3 = ("王五")
my_tuple4 = ()
my_tuple5 = tuple()
my_tuple6 = ("张三",18,("李四",19))
print(my_tuple1)
print(my_tuple2)
print(my_tuple3)
print(my_tuple4)
print(my_tuple5)
print(my_tuple6)
print(my_tuple6[0])
print(my_tuple6[1])
print(my_tuple6[2][0])

'''
 元组的常用操作:
    元组.index(元素):	查找某个数据，如果数据存在返回对应的下标，否则报错
    元组.count(元素)	:统计某个数据在当前元组出现的次数
    len(元组)	:统计元组内的元素个数
'''
print("元组的常用操作:")
print(my_tuple6.index(int("18")))
print(my_tuple6.count("张三"))
print(len(my_tuple6))

print("元组for循环遍历：")
'''元组可便利 for或者while'''
for i in my_tuple6:
    print(i)

i = 0
print("元组while循环遍历：")
while i < len(my_tuple6):
    print(my_tuple6[i])
    i +=1

print("元组内容修改案例：")
tuple1 = ("张三",18 ,("李四",20))
tuple2 = ("王五",19,["赵六",21])
print(tuple1)
print(tuple2)
# tuple1[0] = "田七"
# print(tuple1)  #报错 'tuple' object does not support item assignment

# tuple1[2][0] = "田七" #元组套元组不可修改数据
# print(tuple1) #报错 'tuple' object does not support item assignment

tuple2[2][0] = "田七" #元组套列表可以修改数据  证明了元组一旦定义无法修改，但是列表list可以修改
print(tuple2)  #('王五', 19, ['田七', 21])
print(tuple2[-1])