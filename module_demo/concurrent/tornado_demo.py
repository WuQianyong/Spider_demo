#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

# @Name    : tornado_demo
# @Author  : qianyong
# @Time    : 2017-01-17 13:45

"""
tornado 实现并发爬虫
"""
import time
from datetime import timedelta

from html.parser import HTMLParser
from urllib.parse import urljoin, urldefrag
from tornado import httpclient, gen, ioloop, queues


if __name__ == '__main__':
    pass
