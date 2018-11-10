import time
from datetime import datetime

def __str2time(s):      #一个字符串转换为datetime的时间函数
    t = time.strptime(s,'%Y-%m-%d %H:%M:%S')
    return datetime(*t[:6])

s = __str2time("2017-9-29 22:10:15")
print(s)