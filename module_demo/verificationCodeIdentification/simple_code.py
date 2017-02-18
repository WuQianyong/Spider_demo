#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Time    : 2017/1/5 15:38
# @Author  : wuqianyong
# @File    : simple_code.py
# @Software: PyCharm

"""
简单的验证码识别的 demo
"""

# 导入Image 包 打开图片
from PIL import Image
im = Image.open('image/7039.jpg')

# im_grey = im.convert('L')
# # im_grey.show()
#
# # 二值化处理
# threshold =140
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# out = im_grey.point(table,'1')
# out.show()

# 识别图片
import pytesseract
import os
print(os.getcwd())
print(pytesseract.image_to_string(Image.open('test.png')))






