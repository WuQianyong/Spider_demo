# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:51:33 2017

@author: wqy
"""

"""
展开嵌套的序列
"""

# from collections import Iterable
#
# def flatten(items,ignore_type=(str,bytes)):
#     for x in items:
#         if isinstance(x,Iterable) and not isinstance(x,ignore_type):
#             yield from flatten(x)
#         else:
#             yield x
#
#
# items = [1,2,[3,[4,5,6],7,8],0]
# for x in flatten(items):
#     print(x)

# import array
#
# nums = array.array('i', [1, 2, 3, 4])
# with open('data.bin','wb') as f:
#     f.write(nums)

with open('datafile','wt') as f:
    f.write("hello \n")