'''
和java不同的是python的列表list可以储存多种类型的数据，并且支持嵌套

 列表特点:
可以容纳多个元素（上限为2**63-1、9223372036854775807个）
可以容纳不同类型的元素（混装）
数据是有序存储的（有下标序号）
允许重复数据存在
可以修改（增加或删除元素等）
'''

myList1 = ["张三",1,1.1,True,None]
myList2 = ["张三",15,2.2,["李四",19,5.5]]
print(myList1)
print(myList2)
# 可以正索引也可以反索引
print(myList1[0])
print(myList1[1])
print(myList2[2])
print(myList2[3])
print("反索引：")
print(myList1[-1])
print(myList1[-2])
print(myList1[-3])
print(len(myList1))
# 可以索引嵌套
print("索引嵌套:")
print(myList2[3][0])
print(myList2[3][1])
print(myList2[3][2])


'''
列表的常用方法：
列表.append(元素)	向列表中追加一个元素
列表.extend(容器)	将列表尾部追加一个列表，将列表中的每个元素都追加进来，在原有列表上增加
列表.insert(下标, 元素)	在指定下标处，插入指定的元素
del 列表[下标]	删除列表指定下标元素
列表.pop(下标)	删除列表指定下标元素
列表.remove(元素)	从前向后，删除此元素第一个匹配项
列表.clear()	清空列表
列表.count(元素)	统计此元素在列表中出现的次数
列表.index(元素)	查找指定元素在列表的下标 找不到报错ValueError
len(列表)	统计容器内有多少元素
'''
print("测试列表方法：")
new_list = ["张三",18]
# append()方法 向列表中追加一个元素
new_list.append("测试append（）方法")
print(new_list)

# extend（）方法 将列表尾部追加一个列表，将列表中的每个元素都追加进来，在原有列表上增加
new_list.extend(["extend（）方法"])
print(new_list)

# insert(下标, 元素) 在指定下标处，插入指定的元素
new_list.insert(0,"insert(0, insert)")
print(new_list)

# del 列表[下标] 删除列表指定下标元素
del new_list[0]
print(new_list)

# 列表.pop(下标) 删除列表指定下标元素
new_list.pop(3)
print(new_list)

# 列表.remove(元素)	从前向后，删除此元素第一个匹配项
new_list.remove('测试append（）方法')
print(new_list)

# 列表.clear()	清空列表
new_list.clear()
print(new_list)

new_list.append("李四")
new_list.append(13)
new_list.extend(["王五",13])
print(new_list)

# 列表.count(元素)	统计此元素在列表中出现的次数
print(new_list.count(13))

# 列表.index(元素)	查找指定元素在列表的下标 找不到报错ValueError
print(new_list.index(13))

# len(列表)	统计容器内有多少元素
print(len(new_list))

print(new_list)
# 修改元素
new_list[0] = "赵六"
new_list[-1] = 18
print(new_list)


'''列表的遍历'''
print("列表的遍历：")
for x in new_list:
    print(x)

print("==========")
count = 0
while count < len(new_list):
    print(new_list[count])
    count +=1


