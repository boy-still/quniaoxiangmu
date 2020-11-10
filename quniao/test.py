import sqlite3
import time
import random
DB_Name = 'quniaodata.db'
conn = sqlite3.connect(DB_Name)
print('连接数据库%s成功' % (DB_Name))
times=0
def get_maxday(month,year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day_max = 31
        return day_max
    elif month in [4, 6, 9, 11]:
        day_max = 30
        return day_max
    elif month == 2:
        if year % 4 == 0:
            day_max = 29
            return day_max
        else:
            day_max = 28
            return day_max
while times<2500:
    try:
        timedata = ''
        cursor = conn.cursor()
        year = random.sample(range(2018, 2021), 1)
        month = 2

        day = random.sample(range(1,get_maxday(month,year[0])+1), 1)
        print(month)
        hour = random.sample(range(1,25),1)
        localtime = []
        #print(day)
        localtime.append(year[0])
        localtime.append(month)
        localtime.append(day[0])
        localtime.append(hour[0])
        #print(localtime)
        for i in range(0,4):
            if localtime[i]<10:
                timestr ='0'+str(localtime[i])
            else:
                timestr =str(localtime[i])
            timedata += timestr
        #print(timedata)
        SQL = "INSERT INTO INDEX_QUNIAO(TIME) VALUES('%s');"%timedata
        cursor.execute(SQL)
        conn.commit()
        #print('插入数据到表STUDENT成功')
    except Exception as e:
        print(e)
        # 回滚
        conn.rollback()
        print('插入数据到表QUNIAODATA失败')
    #finally:
        # 关闭数据库
        #conn.close()
        #server_socket.close()
    times+=1
    print(times)