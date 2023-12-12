'''

方法（属性）	说明
today()	    返回当地的当前日期
fromtimestamp(timestamp)	根据给定的时间戮，返回本地日期
min	date    所能表示的最小日期
max	date    所能表示的最大日期
'''
import datetime
import time
date = datetime.date
print(f"date:{date}")
# 返回当地的当前日期
print(f"返回当地的当前日期:{date.today()}")
# 根据给定的时间戮，返回本地日期
print(f"根据给定的时间戮，返回本地日期:{date.fromtimestamp(1575273600)}")
# date.min	date 所能表示的最小日期
print(f"date.min	date 所能表示的最小日期:{date.min}")
# date.max	date 所能表示的最大日期
print(f"date.max	date 所能表示的最大日期:{date.max}")


print("=====================================")
'''
实例方法和属性如下所示：
方法（属性）	                    说明
replace(year, month, day)	    生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性
timetuple()	                    返回日期对应的 struct_time 对象
weekday()	                    返回一个整数代表星期几，星期一为 0，星期天为 6
isoweekday()	                返回一个整数代表星期几，星期一为 1，星期天为 7
isocalendar()	                返回格式为 (year，month，day) 的元组
isoformat()	                    返回格式如 YYYY-MM-DD 的字符串
strftime(format)	            返回自定义格式的字符串
year	                        年
month	                        月
day	                            日
'''
td = datetime.date.today();
# replace(year, month, day)	    生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性
print(f"生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性 :{td.replace(2019,12,3)}")
# timetuple()	                    返回日期对应的 struct_time 对象
print(f"返回日期对应的 struct_time 对象:{td.timetuple()}")
# weekday()	                    返回一个整数代表星期几，星期一为 0，星期天为 6
print(f"返回一个整数代表星期几，星期一为 0，星期天为 6:{td.weekday()}")
# isoweekday()	                返回一个整数代表星期几，星期一为 1，星期天为 7
print(f"返回一个整数代表星期几，星期一为 1，星期天为 7:{td.isoweekday()}")
# isocalendar()	                返回格式为 (year，month，day) 的元组
print(f"返回格式为 (year，month，day) 的元组:{td.isocalendar()}")
# isoformat()	                    返回格式如 YYYY-MM-DD 的字符串
print(f"返回格式如 YYYY-MM-DD 的字符串:{td.isoformat()}")

print("=====================================")
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.fromtimestamp(time.time()))


print("=====================================")

td = datetime.datetime.today()
print(td.date())
print(td.time())
print(td.replace())
print(td.strftime('%Y-%m-%d %H:%M:%S .%f'))