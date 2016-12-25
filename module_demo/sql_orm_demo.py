# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 09:11:24 2016

http://www.jb51.net/article/49789.htm

@author: wqy
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_connect_string = 'mssql+pymssql://root:123456@localhost/demo'
# configure Session class with desired options


# later, we create the engine
engine = create_engine(db_connect_string,echo=True)

# associate it with our custom Session class

# work with the session
Session = sessionmaker(bind=engine)
session = Session()

"""
SQLAlchemy ORM

使用ORM  进行数据库操作
"""

from sqlalchemy import *
from sqlalchemy.types import CHAR,Integer,String
from sqlalchemy.ext.declarative import declarative_base

BaseMode = declarative_base()

def init_db():
    BaseMode.metadata.create_all(engine)
def drop_db():
    BaseMode.metadata.drop_all(engine)
    
class User(BaseMode):
    __tablename__ = 'user2'
    id = Column(Integer, primary_key=True)
    name = Column(CHAR(30)) # or Column(String(30))
    
#init_db()
    
user = User(name='a')
    
    