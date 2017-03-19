#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# =========================================
# nltk_chapter4
# -----------------------------------------
# Fatures:
# Author : qianyong
# Time   : 2017/3/13 10:10
# =========================================
#

import sys, os
import pdb
from nltk.corpus import wordnet as wn


def factorial(n):
    result = 1
    for i in range(n):
        result *= (i + 1)
    return result


def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n - 1)


def size1(s):
    return 1 + sum(size1(child) for child in s.hyponyms())


def main():
    print(sys.argv)
    # pdb.run('factorial(4)')
    # print(factorial2(5))
    dog = wn.synset('dog.n.01')
    print(dog)
    print(size1(dog))
    print(dog.hyponyms())


"""
式构造一个长度为n的旋律
L = 2
S = 1
"""


def vira1(n):
    """
    迭代法
    :param n:
    :return:
    """
    if n == 0:
        return ['']
    elif n == 1:
        return ['S']
    else:
        s = ['S' + prosody for prosody in vira1(n - 1)]
        l = ['L' + prosody for prosody in vira1(n - 2)]
        return s + l


def vira2(n):
    """
    自下而上的动态规划
    :param n:
    :return:
    """
    lookup = [[''], ['S']]
    for i in range(n - 1):
        s = ['S' + prosody for prosody in lookup[i + 1]]
        l = ['L' + prosody for prosody in lookup[i]]
        # print(s+l)
        lookup.append(s + l)

    return lookup[n]


def vira3(n, lookup={0: [""], 1: ["S"]}):
    """
    自上而下的动态规划
    :param n:
    :return:
    """
    if n not in lookup:
        s = ['S' + prosody for prosody in vira3(n - 1)]
        l = ['L' + prosody for prosody in vira3(n - 2)]
        lookup[n] = s + l
    # print(lookup)
    return lookup[n]


from nltk import memoize


@memoize
def vira4(n):
    """
    nltk 自带的默记法
    :param n:
    :return:
    """
    if n == 0:
        return [""]
    elif n == 1:
        return ["S"]
    else:
        s = ['S' + prosody for prosody in vira4(n - 1)]
        l = ['L' + prosody for prosody in vira4(n - 2)]
        return s + l


if __name__ == '__main__':
    print(vira2(5))
    print(vira3(5))
    print(vira4(5))
