# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Time    : 2017/1/6 14:45
# @Author  : wuqianyong
# @File    : read_conf.py
# @Software: PyCharm

from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('db.conf')

print(cfg.sections())
print(cfg.get('installation', 'library'))
print(cfg.getboolean('debug', 'log_errors'))
print(cfg.getint('server', 'port'))
print(cfg.get('server', 'signature'))
cfg.set('server', 'port', '9000')
print(cfg.getint('server', 'port'))
import sys

cfg.write(sys.stdout)
