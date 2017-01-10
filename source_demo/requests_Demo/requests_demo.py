#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Time    : 2017/1/3 16:07
# @Author  : wuqianyong
# @File    : requests_demo.py
# @Software: PyCharm

import requests
tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'
r = requests.get(tarball_url, stream=True)

# import requests
#
#
# r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
# # 这是响应头
# print(r.headers)
# print(r.request.headers)

# with requests.Session() as s:
#     r = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
#     print(r.text)



# s = requests.Session()
# r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
# print(r.text)
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


# resp = requests.get('https://www.baidu.com')
# print(str(resp.content, encoding='utf-8'))
#
# s = requests.Session()
# s.auth = ('user','pass')
# s.headers.update({'x-test':'true'})
# print(s.headers)
# s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print(s.cookies)
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")

# print(r.text)