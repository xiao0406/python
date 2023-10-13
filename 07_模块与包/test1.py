
__all__ = ["add"]
def add (x,y):
    return x+y

def sub(x,y):
    return x-y

print(f"功能测试{add(5,5)}")

'''
# 只在当前文件中运行条件才为True，导入其他文件时均为False
if __name__ == '__main__':
# __main__ 运行时程序的名称
# __name__ 系统自动赋值，不用管
# 在Run时为 __main__ 
# 未Run时为 文件名称

可以用快捷键main
'''

if __name__ == '__main__':
    print(f"这个测试方法不会执行{add(4,4)}")
