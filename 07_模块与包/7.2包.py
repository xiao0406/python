'''
新建包:
新建包后，包内部会自动创建__init__.py文件，这个文件控制着包的导入行为
有__init__.py文件才是python包,没有的话,就是个普通的文件夹

导入包:
import 包名.模块名
包名.模块名.功能名()

限制导入:
可以在__init__.py文件中添加__all__ = ['模块名']，控制允许导入的模块列表
与导入模块类似__all__只针对from 包名.模块名 import *而对其他方式无效
'''
import testPack.test1
import testPack.test2
result1 =  testPack.test1.add(2,1)
print(result1)
result2 =  testPack.test2.sub(2,1)
print(result2)  #可以输出

from testPack import *
print(test1.add(3,4))
# test2  找不到,因为在__init__py文件里定义了test1



'''
第三方包:
在Python程序的生态中，有非常多的第三方包（非Python官方），可以极大的帮助我们提高开发效率，如：
科学计算中常用的：numpy包
数据分析中常用的：pandas包
大数据计算中常用的：pyspark、apache-flink包
图形可视化常用的：matplotlib、pyecharts
人工智能常用的：tensorflow
'''