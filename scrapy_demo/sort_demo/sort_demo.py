#!/home/wqy/anaconda3/bin/python3.5
# -*- coding: utf-8 -*-
# @Time    : 16-12-10 下午9:02
# @Author  : wuqianyong
# @File    : sort_demo.py
# @Software: PyCharm

"""
python 关于排序算法的实现
"""

import random

old_list = random.sample(range(1,30), 10)
print('old:',old_list)

def insert_sort(sort_list):
    """
    插入排序
    :param sort_list:
    :return:
    """
    print('插入排序开始')
    sort_len = len(sort_list)
    if sort_len <=1 :
        return sort_list
    for i in range(1,sort_len):
        key = sort_list[i]
        j = i - 1
        while j>=0 and sort_list[j]>key:
            sort_list[j+1] = sort_list[j]
            j -=1
        sort_list[j+1]=key
        print('i:%d  key:%d  j:%d' % (i, key, j), sort_list)
    return sort_list

def simple_select_sort(sort_list):
    """
    简单选择排序
    :param sort_list:
    :return:
    """
    a_len = len(sort_list)
    num = 0
    if a_len <2 :
        return sort_list
    for i in range(0, a_len-1):
        for j in range(i,a_len):
            if sort_list[j]< sort_list[i]:
                tmp = sort_list[i]
                sort_list[i] = sort_list[j]
                sort_list [j] =tmp
            num+=1
            print(num, sort_list)
    return sort_list

def quick_sort(sort_list,start,end):
    """
    快速排序
    这个函数的作用是，从区间的第一个，最后一个和最中间的位置上选出一个中间大小的值，并把它放置在区间的第一个位置上
这样有效消除预排序的最坏情况
    :param sort_list:
    :return:
    """

    if start > end:
        return
    i, j = start, end
    median(sort_list,start,end)
    tmp = sort_list[start]
    while True:
        while sort_list[j] > tmp and i<j:
            j-=1
        if i<j:
            sort_list[i] = sort_list[j]
            i+=1
        while sort_list [i] <tmp and i<j:
            i+=1
        if i<j:
            sort_list[j] = sort_list[i]
            j -=1
        else:
            break
        print('tmp', tmp, sort_list)
    sort_list[i] =tmp
    print('tmp', tmp, sort_list)
    # print()

    quick_sort(sort_list,start,i-1)
    quick_sort(sort_list,j+1,end)



def median(a,start,end):
    """
    快速排序的 主要方法
    :param a:
    :param start:
    :param end:
    :return:
    """

    center = int((start + end)/2)
    if a[start] > a[center]:
        a[start],a[center] = a[center],a[start]
    if a[start]> a[end]:
        a[start],a[end] = a[end],a[start]
    if a[center] > a[end]:
        a[center], a[end] = a[end], a[center]
    a[start],a[center] = a [center],a[start]
if __name__ == "__main__":


    # demo = insert_sort(old_list)  # 插入排序
    # demo = simple_select_sort(old_list)  # 插入排序
    quick_sort(old_list,0,len(old_list)-1)
    # print('demo' , demo)



