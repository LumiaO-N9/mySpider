import pymysql

config = {
    "host": 'mysql主机地址',
    "user": '用户名',
    "passwd": '密码',
    "db": '数据库名',
    "charset": 'utf8'
}
# 打开数据库连接
db = pymysql.connect(config)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * from comment_jingdong")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print(data)

# 关闭数据库连接
db.close()
