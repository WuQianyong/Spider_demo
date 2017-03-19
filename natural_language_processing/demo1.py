#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# =========================================
# demo1
# -----------------------------------------
# Fatures: NLP的程序
# Author : qianyong
# Time   : 2017/3/7 9:33
# =========================================
#

import pickle


def tag(word):
    """
    assert 断言的用法
    >>> tag(['a'])
    AssertionError: word is error

    :param word:str
    :return:None
    """
    assert isinstance(word, str), "word is error"
    if word in ['a', 'the', 'all']:
        return 'det'
    else:
        return 'noun'


if __name__ == '__main__':
    word = ['a']
    tag(word)
