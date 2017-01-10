#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Time    : 2017/1/3 9:02
# @Author  : wuqianyong
# @File    : zhihu.py
# @Software: PyCharm

"""
python 模拟登录知乎

https://www.zhihu.com/
"""


import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re
import time
import os.path
try:
    from PIL import Image
except:
    pass

# 构造headers

agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

# 使用cookie 信息

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
# print(session.cookies)
#
# try:
#     session.cookies.load(ignore_discard = True)
# except:
#     print('Cookie 未能加载')
#



