#!/home/wqy/anaconda3/bin/python3.5
# -*- coding: utf-8 -*-
# @Time    : 16-12-11 下午5:48
# @Author  : wuqianyong
# @File    : sqlalchemy_demo.py
# @Software: PyCharm

"""
关于 使用sqlalchemy 的一些实例化操作
"""
import sqlalchemy
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy import *
from sqlalchemy.orm import *
engine = sqlalchemy.create_engine('mysql+pymysql://root:microsoft1995@localhost:3306/demo')
# 绑定元信息
metadata = MetaData(engine)

# 创建表格 初始化数据库
user = Table('user', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50)),
            Column('fullname', String(50)),
            Column('password', String(12))
        )

#创建数据表，如果数据表存在则忽视！！！
metadata.create_all(engine)

# 获取数据库连接
conn = engine.connect()

#############一.以每次插入一条记录的方式向user表插入数据##############
#使用查询
i = user.insert()
print(i)
# 插入一组数据

u = dict(name = 'tom', fullname = 'tom smith')
#执行查询，第一个为查询对象，第二个参数为一个插入数据字典，如果插入的是多个对象
#就把对象字典放在列表里边
# r1= conn.execute(i,**u)

# # 每次插入多条记录的方式
# u2 = [{'name': 'tom', 'fullname':'tom smith'},{'name': 'tom2', 'fullname':'tom smith2'},{'name': 'tom3', 'fullname':'tom smith3'}]
# r2 = conn.execute(i,u2)
# print(r2)

# 实现单个表查询

s1 = select([user]).where(user.c.id >1)
print(s1)
r2= conn.execute(s1)
print(r2.fetchall())
