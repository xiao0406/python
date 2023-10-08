bool_name = "wang" == "wang"
bool_name1 = "wang" == "xiao"

bool_age = 18 <= 19
bool_age1 = 18 >= 19
print("类型：%s,结果：%s" % (type(bool_name),bool_name))
print(f"类型{type(bool_name)},结果{bool_name}")
print("类型：%s,结果：%s" % (type(bool_name1),bool_name1))
print("类型：%s,结果：%s" % (type(bool_age),bool_age))
print("类型：%s,结果：%s" % (type(bool_age1),bool_age1))

#  and 等价于java &&  or 等价于java ||
# and 满足两边才为true，or满足一边就为true
print("and or 用例")
age = 1>0 and 2>0  #两真
age1 = 1<0 and 2<0 #两假
age2 = 1>0 and 2<0 #一真一假
age3 = 1>0 or 2<0 #一真一假
age4 = 1<0 or 2>0 #一真一假
print(f"类型是{type(age)},结果是{age}")
print(f"类型是{type(age1)},结果是{age1}")
print(f"类型是{type(age2)},结果是{age2}")
print(f"类型是{type(age3)},结果是{age3}")
print(f"类型是{type(age4)},结果是{age4}")