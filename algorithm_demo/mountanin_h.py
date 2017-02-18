#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

# @Name    : mountanin_h
# @Author  : qianyong
# @Time    : 2017-02-06 9:25

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.
import  random

# game loop

for i in range(8):
    # mountain_h = int(input())  # represents the height of one mountain.
    mountain_h = random.randint(0,9)
    print(mountain_h)