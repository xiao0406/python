'''
基本语法:
1.捕获常规异常
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码

# 未发生错误try全部代码都会执行
# 未发生错误不会执行except中的代码
# 发生错误try中只会执行到报错行为止的代码
# 发生错误会执行except中的代码
'''

try:
    print("r模式打开") # 执行
    f = open("E:/观止.txt", "r") # 报错
    print("r模式打开") # 不执行
except:
    print("w模式打开") # 执行
    f = open("E:/观止.txt", "w") # 执行
    print("w模式打开") # 执行


'''
捕获特定异常
基本语法:
try:
    可能发生错误的代码
except 待捕获异常名 as 别名
    如果出现异常的代码
'''
print("特定异常=================")
try:
    print(name) #未定义变量,报错
except NameError as e:
    print("name未定义变量名,报错")


# try:
#     open("E:/aaa","r")
# except NameError as e:  # 无法捕获,因为这个异常不是NameError(可以定义Exception)
#     print("没有此文件")

try:
    open("E:/aaa","r")
except (NameError,Exception) as e:
    print("没有此文件")
    print(e)   #[Errno 2] No such file or directory: 'E:/aaa'

'''
异常else
else表示的是如果没有异常要执行的代码
实例:
try:
    print(num) # 未定义，报错
except (NameError, ZeroDivisionError) as e:
    print(e) # 打印 name 'num' is not defined
else:
    print("无异常") # 有异常，不执行

'''
print("else 用法:===========")
try:
    name = "张三"
    print(name)
except (TypeError,NameError,Exception) as e:
    print("name异常")
else:
    print("无异常")


'''
异常finally
finally表示的是无论是否异常都要执行的代码
'''
print("测试finally==================")
try:
    print(age)
except (Exception) as e:
    print("age异常")
finally:
    print("无论怎么都要执行")



'''
异常可以传递
'''
print("测试异常的传递============")
def func1():
    print("func1()执行了")
    func2()


def func2():
    num = 1/0
    print("func2()执行了")
    func4()

def func4():
    print("func3()执行了")

# 调用方法一没有异常,然后调用方法2出现异常,捕获,不会调用func3了,最后执行finally
def main():
    try:
        func1()
    except (Exception) as e:
        print("出现异常")
    finally:
        print("main()执行了")

main()