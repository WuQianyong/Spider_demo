# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:51:33 2017

@author: wqy
"""

#
# """
# 展开嵌套的序列
# """
#
#
# # from collections import Iterable
# #
# # def flatten(items,ignore_type=(str,bytes)):
# #     for x in items:
# #         if isinstance(x,Iterable) and not isinstance(x,ignore_type):
# #             yield from flatten(x)
# #         else:
# #             yield x
# #
# #
# # items = [1,2,[3,[4,5,6],7,8],0]
# # for x in flatten(items):
# #     print(x)
#
# # import array
# # `
# # nums = array.array('i', [1, 2, 3, 4])
# # with open('data.bin','wb') as f:
# #     f.write(nums)
#
# def avg(first, *rest):
#     return (first + sum(rest)) / (1 + len(rest))
#
#
# # print(avg(1,2))
# # print(avg(1,3,45,6))
#
# def add(x: int, y: int):
#     return x + y
#
#
# #
# # print(type(add(1, 2)))
# # print(add(1, 2))
# # help(add)
# # # help(int)
# # print(add.__annotations__)
# """
# 定义一个单方法的类
# """
# from urllib.request import urlopen
#
#
# class UrlTemplate:
#     def __init__(self, template):
#         self.template = template
#
#     def open(self, **kwargs):
#         return urlopen(self.template.format_map(kwargs))
#
#
# # 这个类-可以被更简单的函数代替
# def urltemplate(templete):
#     def opener(**kwargs):
#         return urlopen(templete.format_map(kwargs))
#
#     return opener
#
#
# #
# # yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# # for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
# #     print(line.decode('utf-8'))
#
#
# # 带额外信息的回调函数
# def apply_async(func, args, *, callback):
#     result = func(*args)
#     callback(result)
#
#
# def print_result(result):
#     print('Got', result)
#
#
# def add(x, y):
#     return x + y
#

# print(apply_async(add, (2, 3), callback=print_result))
#
# """
# 内联回调函数
# """
#
#
# def apply_async(func, args, *, callback):
#     result = func(*args)
#     callback(result)
#
#
# from queue import Queue
# from functools import wraps
#
#
# class Async:
#     def __init__(self, func, args):
#         self.func = func
#         self.args = args
#
#
# def inlined_async(func):
#     @wraps(func)
#     def wrapper(*args):
#         f = func(*args)
#         result_queue = Queue()
#         result_queue.put(None)
#         while True:
#             result = result_queue.get()
#             try:
#                 a = f.send(result)
#                 apply_async(a.func, a.args, callback=result_queue.put)
#             except StopIteration:
#                 break
#
#     return wrapper
#
#
# def add(x, y):
#     return x + y
#
#
# @inlined_async
# def test():
#     r = yield Async(add, (2, 3))
#     print(r)
#     r = yield Async(add, ('hello', 'world'))
#     print(r)
#     for n in range(10):
#         r = yield Async(add, (n, n))
#         print(r)
#
#     print('GoodBye')
#
#
# # test()
#
#
# class Pair:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return 'Pair({0.x!r}, {0.y!r})'.format(self)
#
#     def __str__(self):
#         return '({0.x!s}, {0.y!s})'.format(self)
#
#
# p = Pair(3, 4)
# print('p is {0!r}'.format(p))
#
# _formats = {
#     'ymd': '{d.year}-{d.month}-{d.day}',
#     'mdy': '{d.month}/{d.day}/{d.year}',
#     'dmy': '{d.day}/{d.month}/{d.year}'
# }
#
#
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def __format__(self, code):
#         if code == '':
#             code = 'ymd'
#         fmt = _formats[code]
#         return fmt.format(d=self)
#
#
# d = Date(2012, 12, 21)
# print(format(d, 'mdy'))
#

"""
创建可管理属性
"""

#
# class Person:
#     def __init__(self, first_name):
#         self.first_name = first_name
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._first_name = value
#
#     @first_name.deleter
#     def first_name(self):
#         raise AttributeError('类错误')
# #
# #
# # a = Person('wuqianyong')
# # print(a.first_name)
# # a.first_name = '42'
# # print(a.first_name)
# # del a.first_name
#
# """
# 调用父类方法
# """
#
# class A:
#     def spem(self):
#         print('A.spem')
#
# class B(A):
#     def spem(self):
#         print('B.spem')
#         # super().spem()
#
#
# a = A()
# a.spem()
#
# b = B()
# b.spem()

"""
删除互为相反数的观测
"""

import random


def oppsite_num(the_tuple):
    """
    获得  相反 的观测
    :param the_tuple:
    :return:
    """
    if isinstance(the_tuple, int):
        return -the_tuple
    else:
        opp_tuple = tuple([-a for a in the_tuple])
        return opp_tuple


# 1:生成随机整数数组,假设观测有两个变量
# record_1 = [random.randint(-100, 100) for i in range(1, 5000)]
# record_2 = [random.randint(-100, 100) for i in range(1, 5000)]
# # 两个变量组合成一个数据集
# data_col1 = list(zip(record_1, record_2))


# 2: 只有一个变量
import random
# 生成观测数据
data_col1 = [random.randint(-10, 10) for i in range(20)]
print(data_col1)
# 将list 转换成dict
data_dict = {}
for i in range(len(data_col1)):
    if data_col1[i] not in data_dict:
        data_dict[data_col1[i]] = [i]
    else:
        data_dict[data_col1[i]].append(i)
print(data_dict)
# 查找 互为相反观测的index
del_index = []
for i in data_col1:
    if i == 0:
        continue
    if data_dict.has_key(-i):
        del_index.extend(data_dict[i])
print(del_index)
# 新建一个 list,保存结果
new_data_col = [data_col1[a] for a in range(len(data_col1)) if a not in del_index]
print('new_data: ',new_data_col)




# del_index = []
# for i in range(len(data_col1)):
#     one = data_col1[i]
#     opp_tuple = oppsite_num(one)
#     if isinstance(one, tuple):
#         if one == tuple([0 for i in range(len(one))]):
#             continue
#
#     if one == 0:
#         continue
#     if opp_tuple in data_col1:
#         del_index.append(i)
#         print(one)
#         # print(opp_tuple)
#
#         print('index: ', data_col1.index(one), '存在相反的观测 index: ', data_col1.index(opp_tuple))
# del_index = sorted(list(set(del_index)))
# print('需要删除的', del_index)
#
# # 根据存储 的index remove
# new_data_col1 = [data_col1[i] for i in range(len(data_col1)) if i not in del_index]
# print(new_data_col1)
# print('len: ', len(new_data_col1))
