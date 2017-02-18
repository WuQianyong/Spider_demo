#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Time    : 2017/1/10 17:42
# @Author  : wuqianyong
# @File    : sqlalchemy_orm_demo2.py
# @Software: PyCharm




import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.sql import func

if __name__ == "__main__":
    engine_str = 'mssql+pymssql://root:123456@localhost/VsatHKStock?charset=utf8'
    engine = sqlalchemy.create_engine(engine_str)
    session = Session(engine)

    # 下面这两句话就完成了ORM映射 Base.classes.XXXX即为映射的类
    # Base.metadata.tables['XXX']即为相应的表
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()
    # 查询操作
    # result = session.query(Base.classes.T_EquityPosition)
    # print(result)
    # # 插入操作
    # item = Base.classes.T_EquityPosition(StockCode = '[20000.HK')
    # print(item)
    # item = Base.classes.users(name='lxq', password='1234')
    T_EquityPosition = Base.classes.T_EquityPosition
    result = session.query(func.distinct(T_EquityPosition.StockCode))
    print(list(result))


    for a in result:
        print(a)
