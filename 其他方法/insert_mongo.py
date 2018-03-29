# -*- coding: utf-8 -*-
from copy import deepcopy
import pymongo


class Mongodb(object):
    def __init__(self):
        self.host = u"IP地址"
        self.port = 27017
        self.database_name = u"连接的数据库"
        self.user = u"用户名"
        self.password = u"密码"
        self.collection_name = u"插入的集合名称"

        connect = pymongo.MongoClient(host=self.host, port=self.port)
        database = connect[self.database_name]
        database.authenticate(self.user, self.password)

        self._insert_sql = database[self.collection_name]

    def insert_one(self, value):
        self._insert_sql.insert_one(value)

    def insert_many(self, value):
        self._insert_sql.insert_many(value)


if __name__ == "__main__":
    data1 = [
        {"key1": "value1"},
        {"key2": "value2"},
        {"key3": "value3"}
    ]
    # 对相同的数据进行 insert_one 和 insert_many 会出现pymongo.errors.BulkWriteError: batch op errors occurred的错误。
    # 故此对源对象进行深拷贝
    data2 = deepcopy(data1)

    mg = Mongodb()

    # # 逐条插入
    for d in data1:
        mg.insert_one(d)

    # 多条插入
    mg.insert_many(data2)
