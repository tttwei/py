import pymysql

# 创建连接
conn = pymysql.connect(host='localhost', user='root', password='123456', database='machine_trading', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()
sql = "select * from bk0475 where 日期 > '2017-01-01' and 日期 < '2017-03-01' limit 0,1"
cursor.execute(sql)
fetchall = cursor.fetchall()

print(fetchall[0][0])
