import time
'''
0	tm_year（年）	        如：1945
1	tm_mon（月）	            1 ~ 12
2	tm_mday（日）	        1 ~ 31
3	tm_hour（时）	        0 ~ 23
4	tm_min（分）	            0 ~ 59
5	tm_sec（秒）	            0 ~ 61
6	tm_wday（周）	        0 ~ 6
7	tm_yday（一年内第几天）	1 ~ 366
8	tm_isdst（夏时令）	    -1、0、1
'''
t = time.localtime()
print(f"当前时间:{t}")
print(f"年:{t.tm_year}")
print(f"当前时间{t[0]}/{t[1]}/{t[2]}")


'''

函数（常量）	                         说明
time()	                            返回当前时间的时间戳
gmtime([secs])	                   将时间戳转换为格林威治天文时间下的 struct_time，可选参数 secs 表示从 epoch 到现在的秒数，默认为当前时间
localtime([secs])	               gmtime() 相似，返回当地时间下的 struct_time
mktime(t)	                       ocaltime() 的反函数
asctime([t])	                   接收一个 struct_time 表示的时间，返回形式为：Mon Dec  2 08:53:47 2019 的字符串
ctime([secs])	                  ctime(secs) 相当于 asctime(localtime(secs))
strftime(format[, t])	          格式化日期，接收一个 struct_time 表示的时间，并返回以可读字符串表示的当地时间
sleep(secs)	                      停执行调用线程指定的秒数
altzone	                          本地 DST 时区的偏移量，以 UTC 为单位的秒数
timezone	                      地（非 DST）时区的偏移量，UTC 以西的秒数（西欧大部分地区为负，美国为正，英国为零）
tzname	                          两个字符串的元组：第一个是本地非 DST 时区的名称，第二个是本地 DST 时区的名称

'''
import time
# 返回当前时间的时间戳
print(f"当前时间戳:{time.time()}")
# 将时间戳转换为格林威治天文时间下的 struct_time，可选参数 secs 表示从 epoch 到现在的秒数，默认为当前时间
print(f"格林威治天文时间(默认):{time.gmtime()}")
print(f"格林威治天文时间(传入时间戳):{time.gmtime(1575273600)}")
# localtime([secs])
print(f"localtime([secs]):{time.localtime()}")
# asctime([t])
print(f"asctime([t]):{time.asctime()}")
# strftime(format[, t])   日期格式化
print(f"日期格式化:{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())}")
