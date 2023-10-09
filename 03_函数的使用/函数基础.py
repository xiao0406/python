''''
定义:组织好的，可重复使用的，用来实现特定功能的代码段（类似于java的方法）
'''

'''
# 定义
def 函数名(传入参数):
    函数体
    return 返回值
# 使用
函数名(传入参数)
'''

# 例子 定义一个长度的函数
# def getLet(data):
#     count = 0
#     for i in data:
#         count += 1
#     return count
#
#
# print(getLet("100"))

# def testNone(age):
#     if age > 18:
#         return age
#
#
# print(type(testNone(17)))
number = 500


# global用法  修改全局变量，相当于java的this
# def testGlobal():
#     global number
#     number = 100
#     return number
#
#
# print(testGlobal())
# print(number)


# python的返回值可以有多个，并且类型可以不用
def test():
    return 11, 1.111, "王", True, None


# x ,y ,z,q,w = test()
# print(x,y,z,q,w)
# print(test())
# for x in test():
#     print(x)
# print(test()[0])
# print(test()[1])
# print(test()[2])


"""
方法的参数传递： 
1.顺序传参
2.可以通过‘键=值’传递
3.缺省传参，可以定义默认值
4.不定长传参
    4.1:以*号标记一个形式参数，以元组的形式接受参数
    4.2:关键字不定长传递以**号标记一个形式参数，以字典的形式接受参数,参数是“键=值”形式的形式的情况下, 所有的“键=值”都会被kwargs接受, 同时会根据“键=值”组成字典.
"""


# 1.顺序传参
def test1(name, age, money):
    print(f"{name}已经{age}岁了，身价为{money}万")


# test1("张三", 18, 100)


# 2.可以通过‘键=值’传递
def test2(name, age, money):
    print(f"{name}已经{age}岁了，身价为{money}万")
#
# test2(name='李四', money=200, age=30)

# 3.缺省传参，可以定义默认值
def test3(name, age, money=1000):
    print(f"{name}已经{age}岁了，身价为{money}万")
#
# test3(name='王五', age=40)
# test3('王五',40)

# 4.1:以*号标记一个形式参数，以元组的形式接受参数

def test4(*ages):

    print(ages[0])
    print(ages[1])
    print(ages[2])
    print(ages)
# test4("王",44,2.2)
# test4(name="王",age=44,num=2.2)  #报错 TypeError: test4() got an unexpected keyword argument 'name'

# 4.2:关键字不定长传递以**号标记一个形式参数，以字典的形式接受参数,参数是“键=值”形式的形式的情况下, 所有的“键=值”都会被kwargs接受, 同时会根据“键=值”组成字典.
def test5(**ages):

    print(ages)
# test5(name="王",age=44,num=2.2)


# ======================
def func1():
    print("hello world~")
func = func1
# func() # 打印 hello world~

# def add(x, y):
#     return x + y
def compute(add):
    result = add(6, 3)
    print(result)
# compute(add)
# 输出 9

'''
lambda 的使用
'''

def compute(add):
    result = add(6, 3)
    print(result)
# 输出 9
# compute(lambda x, y: x + y)
# 等效于
# def add(x, y):
#     return x + y
# def compute(add):
#     result = add(6, 3)
#     print(result)
# # 输出 9
# compute(add)


def test7(aaa):
    print(aaa(1,2))
test7(lambda x,y:x+y)


