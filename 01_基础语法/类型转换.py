# 类型转换   int（x） 将类型转换为 int
name = int(111.111)
name_type = type(name)
# str转int里面必须是常量，不能是浮点类型。比如 "222" 可以执行，"222.222"运行报错
name1 = int("222")
name1_type = type(name1)
print("类型为：",name_type,"结果为：",name)
print("类型为：",name1_type,"结果为：",name1)

# float(x) 将类型转换为 float
name = float(1111111)
name_type = type(name)
name1 = float("333.333")
name1_type = type(name1)
print("类型为：",name_type,"结果为：",name)
print("类型为：",name1_type,"结果为：",name1)

# str（x） 将类型转换为str
name = str(111)
name_type = type(name)
print("类型为：",name_type,"结果为：",name)