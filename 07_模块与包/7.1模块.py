'''
语法:
[from 模块名] import [模块|类|变量|函数|*] [as 别名]
# *表示导入所有

常见的组合方式:
import 模块名
from 模块名 import 类、变量、方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名
'''

'''
用法一:
# 导入
import 模块名
import 模块名1，模块名2

# 使用
模块名.功能名()

'''
import time

# print("开始")
# time.sleep(3) #睡3秒
# print("结束")

'''
用法二:
# 导入
from 模块名 import 功能名

# 使用
功能名()
'''

from time import sleep
# print("用法二开始")
# sleep(3)
# print("用法二结束")



'''
用法3:
# 导入一：模块定义别名
import 模块名 as 别名

# 使用一：
别名.功能名()

# 导入二：功能定义别名
from 模块名 import 功能 as 别名

# 使用二：
别名()

'''
import time as t
from time import sleep as s

print("用法3开始了")
t.sleep(1)
print("用法3测试别名")
s(1)
print("用法3结束了")


'''
用法4:
# 导入
from 模块名 import *

# 使用
功能名()

'''
from time import *
print("用法4开始了==")
print(f"当前时间:{time()}")
sleep(3)
print(f"当时时间{time()}")
print("用法4结束了")


'''
可以自定义py文件进行导入模块
if __name__ == '__main__'定义的方法不会被执行
__all__变量定义了才会被执行
'''
# import test1
#
# print(test1.add(1,2))
# print(test1.sub(2,1))


'''
如果一个模块文件中有__all__变量，当使用from xxx import *导入时，只能导入这个列表中的元素
'''
# from test1 import *
# print(add(1,2))
# print(sub(3,1)) #找不到此方法.因为test1里有__all__ = ["add"]
