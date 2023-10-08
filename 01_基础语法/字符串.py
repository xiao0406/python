
# 三种方式
name1 = '李'
name2 = "杨"
name3 = """欢"""
print(name1)
print(name2)
print(name3)

# 字符串拼接
print("字符串拼接:")
name = "李" + "杨欢"
print(name)
name4 = "王"
print(name4 + "xy")

# 字符串格式化：
# %表示占位   s表示放入位置
print("字符串格式化：")
name = "xy"
message = "w %s" % name
print(message)

# 多变量拼接  必须加（），顺序拼接
print("多变量拼接:")
name  = "x"
name1 = "y"
message = "w %s %s" % (name,name1)
print(message)


# %s	将内容转换成字符串，放入占位位置
# %d	将内容转换成整数，放入占位位置
# %f	将内容转换成浮点型，放入占位位置

name  = 2
name1 = 3.4
message = "整数拼接，整数：%d ，小数：%f"  % (name,name1)
print(message)
