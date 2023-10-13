'''
字符串是字符的容器，一个字符串可以存放任意数量的字符。
同元组一样,字符串是一个无法修改的数据容器
'''
name = "abcdefa"
print(name[0])
print(name[1])
print(name[-1])

'''
字符串的常用操作:
字符串[下标]	根据下标索引取出特定位置字符
字符串.index(字符串）	查找给定字符的第一个匹配项的下标
字符串.replace(字符串1, 字符串2)	将字符串内的全部字符串1，替换为字符串2 不会修改原字符串，而是得到一个新的
字符串.split(字符串)	按照给定字符串，对字符串进行分隔 不会修改原字符串，而是得到一个新的列表
字符串.strip() 字符串.strip(字符串)	移除首尾的空格和换行符或指定字符串
字符串.count(字符串)	统计字符串内某字符串的出现次数
len(字符串)	统计字符串的字符个数
'''
print(name.index("a"))
print(name.index("b"))
print(name.replace("a","b"))
name1 = "王 晓 阳"
print(name1.split(" "))
name2 = "     Hello    World   122222    "
print(name2.strip())
print(name2.strip().strip("2"))
print(name.count("a"))
print(len(name))

print("=====================")
aaa = "abcde"
bbb = ''
count = 0
while count <len(aaa):
    bbb += aaa[len(aaa)-count -1]
    count +=1

print(bbb)

