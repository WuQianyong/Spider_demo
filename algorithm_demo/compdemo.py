#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/4 19:06
# @Author  : wuqianyong
# @File    : chatting_npl_demo.py
# @Software: PyCharm


"""
随机漫步

"""


import numpy as np
import random
import matplotlib.pylab as plt
import pandas as pd
from pandas import DataFrame

data = DataFrame(np.arange(6).reshape((2,3)),
                 index=pd.Index(['Ohio','Colorado'],name='state',),
                 columns=pd.Index(['one','two','three'],name  = 'number'))
#print(data)
#print(data['columns']
import math
print('The value of PI {} is approximately {}.'.format(math.pi,10))