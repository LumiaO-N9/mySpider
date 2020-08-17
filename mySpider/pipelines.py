# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class MyspiderPipeline:
    def process_item(self, item, spider):
        return item


# 自定义item处理的pipeline
# 需要在settings.py 中指定 一下
class JingDongPipeline:
    def __init__(self):
        # 创建连接
        # 打开数据库连接
        self.config = {
            "host": 'mysql主机地址',
            "user": '用户名',
            "passwd": '密码',
            "db": '数据库名',
            "charset": 'utf8'
        }

        self.db = pymysql.connect(host=self.config['host'],
                                  user=self.config['user'],
                                  passwd=self.config['passwd'],
                                  db=self.config['db'],
                                  charset=self.config['charset'],
                                  )
        self.db.autocommit(True)

    def process_item(self, item, spider):
        id = item["id"]
        nickname = item["nickname"]
        content = item["content"]
        score = item["score"]
        # 将数据保存到MySQL中

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        args = (id, nickname, content, score)
        sql = 'insert into comment_jingdong values (%d,"%s","%s",%d)'
        print(sql % args)
        cursor.execute(sql % args)
