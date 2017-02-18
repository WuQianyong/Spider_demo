#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Time    : 2017/1/4 10:32
# @Author  : wuqianyong
# @File    : app.py
# @Software: PyCharm

import requests
import re
import pandas as pd


def spider_main():
    app_style = {
        '-10': '腾讯软件',
        '122': '购物',
        '102': '阅读',
        '110': '新闻',
        '103': '视频',
        '108': '旅游',
        '115': '工具',
        '106': '社交',
        '101': '音乐',
        '119': '美化',
        '104': '摄影',
        '114': '理财',
        '117': '系统',
        '107': '生活',
        '112': '出行',
        '118': '安全',
        '111': '教育',
        '109': '健康',
        '105': '娱乐',
        '100': '儿童',
        '113': '办公',
        '116': '通讯'}
    # app_style = {
    #     '-10': '腾讯软件'}
    # 这是头信息
    header = {
        'User - Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


    # 抓取数据结果
    spider_result = []

    for style_num in app_style:
        url = (
            'http://sj.qq.com/myapp/cate/appList.htm?orgame=1&categoryId={}&pa'
            'geSize=20000&pageContext=0'.format(style_num))
        req = requests.get(url, headers=header).text

        # 正则匹配
        reg_str = re.compile(r'\"appName\":\"(.*?)\"')
        app_list = reg_str.findall(req)
        editor_list = re.compile(r'editorIntro\":\"(.*?)\"').findall(req)
        print('changdu:{}{}'.format(len(app_list),len(editor_list)))
        for app_name in zip(app_list,editor_list):
            one_item = {'style_num': style_num,
                        'style': app_style.get(style_num),
                        'app_name': app_name[0],
                        'editor_info':app_name[1]}
            spider_result.append(one_item)
            print('抓取到：', str(one_item))

    # 数据转换成 Dataframe 类型
    spider_df = pd.DataFrame(spider_result)
    # print(spider_df)
    writer = pd.ExcelWriter('app.xlsx')
    spider_df.to_excel(writer, 'app', index=False)
    writer.save()


if __name__ == '__main__':
    spider_main()
