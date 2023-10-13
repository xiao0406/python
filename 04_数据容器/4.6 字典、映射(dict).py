'''
基本格式
# 定义字典
变量名称 = {key:value, key:value, key:value}
# 定义空字典
变量名称 = {}
变量名称 = dict()


使用{}存储原始，每一个元素是一个键值对
每一个键值对包含Key和Value（用冒号分隔）
键值对之间使用逗号分隔
Key和Value可以是任意类型的数据（key不可为字典）
Key不可重复，重复会对原有数据覆盖
'''

dict1 = {"姓名": "张三", "年龄": 18, "性别": "男", "姓名": "张三"}
dict2 = {"姓名": "李四", "年龄": 18, "性别": "男"}
dict3 = {}
dict4 = dict()
dict5 = {"张三": {"成绩": {"语文": 110, "数学": 100}},
         "李四": {"成绩": {"语文": 110, "数学": 100}}}
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)

# 数据获取
print("数据获取===============")
print(dict1["姓名"])
print(dict5["张三"])
print(dict5["李四"])


'''
字典的常用操作
字典[Key]	获取指定Key对应的Value值
字典[Key] = Value	添加或更新键值对
字典.pop(Key)	取出Key对应的Value并在字典内删除此Key的键值对
字典.clear()	清空字典
字典.keys()	获取字典的全部Key，可用于for循环遍历字典
len(字典)	计算字典内的元素数量
'''
print("字典的常用操作=====================")
new_dict1 = {"姓名": "张三", "年龄": 18}
print(new_dict1)
new_dict1["姓名"] = "李四"
print(new_dict1)
new_dict1["性别"] = "男"
print(new_dict1)

print(f"测试pop()方法:{new_dict1.pop("姓名")}")
print(new_dict1)

print(print(f"测试keys()方法:{new_dict1.keys()}"))
print(len(new_dict1))

print("=便利==========")
for i in new_dict1:
    print(f"{i}:{new_dict1[i]}")

for key in new_dict1.keys():
    print(f"{key}:{new_dict1[key]}")