# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 13:25
# @Author  : CRJ
# @File    : conn.py
# @Software: PyCharm
# @Python3.6
"""
    提供redis、mysql等连接对象实例

"""
import pika
import pymysql
import redis
from dbutils.pooled_db import PooledDB

import settings

# 从redis连接池中获取连接对象
redis_pool = redis.ConnectionPool(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD,
    max_connections=512,
)
redis_conn = redis.Redis(connection_pool=redis_pool)


# 创建rabbitmq连接
rabbitmq_conn = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_HOST))

# 从mysql连接池中获取连接对象
mysql_pool = PooledDB(
    pymysql,
    50,
    host=settings.MYSQL_HOST,
    port=settings.MYSQL_PORT,
    user=settings.MYSQL_USER,
    passwd=settings.MYSQL_PASSWORD,
    db=settings.MYSQL_DB,
    charset=settings.MYSQL_CHARSET,
)

"""
show variables like 'max_connections'; 查看数据库最大连接数

set global max_connections=1000  修改

"""
