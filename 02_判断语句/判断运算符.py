age = 17
print("if else 用法：")
if age < 18:
    print("年龄未满18")
else:
    print("年龄已满18")

print("if-elif-else 用法：")
if age < 18:
    print("年龄小与18")
elif age == 18:
    print("等于18")
else:
    print("大于18")

print("嵌套使用")
money = 100
if age < 18:
    print("年纪小于18")
    if money < 100:
        print("金额小于100")
    else:
        print("金额大于等于100")
else:
    print("年纪大于等于18")
