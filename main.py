import requests
import time
 
# 格式化成2016-03-20 11:45:39形式
now_time = time.strftime("%Y-%m-%d", time.localtime())
notice = '今天是'+str(now_time)+'哦，别忘记恋爱打卡~'
requests.get('https://api2.pushdeer.com/message/push?pushkey=【key】&text='+notice)