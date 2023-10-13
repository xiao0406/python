'''
(1) 文件的打开
在Python，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件
基本语法：
open(name, mode, encoding)
# name：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。
# mode：设置打开文件的模式(访问模式)：只读、写入、追加等(r->read(读取)，w->write(写入)，a->append(追加))
# encoding:编码格式（推荐使用UTF-8）
'''


'''
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，原有内容会被删除。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，新的内容将会被写入到已有内容之后。 如果该文件不存在，创建新文件进行写入
'''
f1 = open("E:/bill.txt", "r", encoding="UTF-8")
f2 = open("E:/bill1.txt", "w", encoding="UTF-8")
f3 = open("E:/bill2.txt", "a", encoding="UTF-8")
# encoding的顺序不是第三位，所以不能用位置参数，用关键字参数直接指定
# f是open函数的文件对象，可以使用对象.属性或对象.方法对其进行访问


'''
(2) 文件的读取
操作	功能
文件对象.read(num)	读取指定长度字节 不指定num读取文件全部
文件对象.readline()	读取一行
文件对象.readlines()	读取全部行，返回列表
for line in 文件对象	for循环文件行，一次循环得到一行数据
文件对象.close()	关闭文件对象
with open() as f	通过with open语法打开文件，可以自动关闭
'''
# E:/bill.txt  :这个文件有9行,每行对应的内容为行数,先读取
# r1 = f1.read()
# print(r1)
# r2 = f1.readline()
# print(r2)
# r3 = f1.readlines()
# print(r3)

# d循环读取文件
# for e in f1:
#     print(e)
# f1.close()


# with open("E:/bill.txt", "r", encoding="UTF-8") as f:
#   print(f.readlines())


'''
3.文件的写入
  f = open("C:/code/test.txt", "w")
# 文件如果不存在，使用”w”模式，会创建新文件
# 文件如果存在，使用”w”模式，会将原有内容清空
# 2.文件写入
f.write('hello world')
# 3. 内容刷新
f.flush()
'''
f4 = open("E:/bill4.txt","w")
# print(f"原始f4的文件{f4.read()}")
f4.write("测试文件写入")
f4.write("aaaaaaaa")
f4.flush()
r4 = open("E:/bill4.txt","r")
print(r4.read())



a4 = open("E:/bill4.txt","a")
a4.write("追加内容")
a4.flush()
r5 = open("E:/bill4.txt","r")
print(r5.read())





