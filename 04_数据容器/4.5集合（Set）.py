'''
集合 set：
不支持元素的重复（自带去重功能）、并且内容无序
'''

'''
基本格式：
# 定义集合
变量名称 = {元素1, 元素2, 元素3, 元素4, 元素5}
# 定义空集合
变量名称 = set()
'''
my_set1 = {"张三", 18, "男", 18}
my_set2 = set()
my_set3 = {}
print(my_set1)
print(my_set2)
print(my_set3)

'''
集合的便利,不支持索引所以不能用whild
'''
print("索引的遍历=============")
for i in my_set1:
    print(i)

'''
 集合的常用操作
集合.add(元素)	集合内添加一个元素
集合.remove(元素)	移除集合内指定的元素
集合.pop()	从集合中随机取出一个元素
集合.clear()	将集合清空
集合1.difference(集合2)	得到一个新集合，内含2个集合的差集 原有的2个集合内容不变
集合1.difference_update(集合2)	在集合1中，删除集合2中存在的元素 集合1被修改，集合2不变
集合1.union(集合2)	得到1个新集合，内含2个集合的全部元素 原有的2个集合内容不变
len(集合)	得到一个整数，记录了集合的元素数量
'''
print("集合的常用操作=============")
my_set4 = set()
print(my_set4)
my_set4.add("张三")
my_set4.add("13")
my_set4.add("13")
print(f"add()用法{my_set4}")
my_set4.remove("13")
print(f"remove()用法{my_set4}")
print(f"pop用法:{my_set4.pop()}")

# 集合1.difference(集合2)	得到一个新集合，内含2个集合的差集 原有的2个集合内容不变
# 集合1.difference_update(集合2)	在集合1中，删除集合2中存在的元素 集合1被修改，集合2不变
new_my_set1 = {"张三", 18, "男"}
new_my_set2 = {"李四", 18, "男"}
difference_set = new_my_set1.difference(new_my_set2)
print(f"集合1.difference(集合2)用法:{difference_set}")
new_my_set1.difference_update(new_my_set2)
print(f"new_my_set1:{new_my_set1}")
print(f"new_my_set2:{new_my_set2}")

# 集合1.union(集合2)	得到1个新集合，内含2个集合的全部元素 原有的2个集合内容不变
union_set = new_my_set1.union(new_my_set2)
print(union_set)

#  交集:intersection()
set1 = {"张三",18,"男"}
set2 = {"翠花",18,"女"}
print(set1.intersection(set2))