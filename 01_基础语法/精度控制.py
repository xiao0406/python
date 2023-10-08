# m，控制宽度，要求是数字（很少使用）,设置的宽度小于数字自身，不生效
#
# .n，控制小数点精度，要求是数字，会进行小数的四舍五入

age = 1
money = 1.55
message = "年龄为：%1d ,金额为：%.1f" % (age,money)
print(message)

# f"内容{变量}"的格式来快速格式化
age = 15
money = 12.1
message =f"年龄{age},身价：{money}"
print(message)

qqqqq