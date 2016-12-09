#!/home/wqy/anaconda3/bin/python3.5
# -*- coding: utf-8 -*-
# @Time    : 16-12-9 上午11:02
# @Author  : wuqianyong
# @File    : pymssql_demo.py
# @Software: PyCharm

import pymysql

conn = pymysql.connect(host='127.0.0.1',user = 'root' ,password = 'microsoft1995', database = 'mysql')
print(1)
cur = conn.cursor()
cur.execute('show tables;')
row = cur.fetchall()
print(row)
conn.close


