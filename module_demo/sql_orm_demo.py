# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 09:11:24 2016

http://www.jb51.net/article/49789.htm

@author: wqy
"""
#
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
#
#
# db_connect_string = 'mssql+pymssql://root:123456@localhost/demo'
# # configure Session class with desired options
#
#
# # later, we create the engine
# engine = create_engine(db_connect_string,echo=True)
#
# # associate it with our custom Session class
#
# # work with the session
# Session = sessionmaker(bind=engine)
# session = Session()

"""
SQLAlchemy ORM

使用ORM  进行数据库操作
"""

# from sqlalchemy import *
# from sqlalchemy.types import CHAR,Integer,String
# from sqlalchemy.ext.declarative import declarative_base
#
# BaseMode = declarative_base()
#
# def init_db():
#     BaseMode.metadata.create_all(engine)
# def drop_db():
#     BaseMode.metadata.drop_all(engine)
#
# class User(BaseMode):
#     __tablename__ = 'user2'
#     id = Column(Integer, primary_key=True)
#     name = Column(CHAR(30)) # or Column(String(30))
#
# #init_db()
#
# user = User(name='a')
#
#
from sqlalchemy import *

engine = create_engine('sqlite:///foo.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 内工厂函数，将不同数据库引擎创建一个基类
Base = declarative_base()       # 首字母大写表示这是一个类

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>"%(
            self.name, self.fullname, self.password
        )

# 创建数据表，如果没有 注释，会自动覆盖
# Base.metadata.create_all(engine)


# 创建回话，进行添加数据
ed_user = User(name='ed', fullname='ed jhon', password='sjlffl')
print(ed_user)
Session = sessionmaker(bind=engine)
session = Session()
session.add(ed_user)
session.commit()
print(session.query(User).all())

