# -*- coding: utf-8 -*-
"""

导入目标价
Created on Thu Dec 29 15:18:48 2016

@author: wqy
"""
import numpy
import pandas as pd
import pymssql
from pandas import ExcelWriter

def get_select(one_dict):
    """
    通过数据连接，获得获得  研究报告编码（T_ReportFellow）
    """

    select_sql = ('select reportCode from T_ReportStock  where '
                  'stockcode = \'{code}\' and reportcode in (SELECT '
                  ' reportcode FROM  T_ReportFellow where fellowcode'
                  ' in (SELECT code FROM T_ResearchFellow where name'
                  '= \'{name}\') and reportcode in( SELECT CODE FROM '
                  'T_ReportBaseInfo where researchagency=(SELECT CODE'
                  ' FROM T_ResearchAgency  where namecn = \'{agency}\')'
                  ' and reportdate  = \'{date}\'))'.format(
                      code=one_dict.get('code'),
                      name=one_dict.get('research'),
                      agency=one_dict.get('agency'),
                      date=one_dict.get('ycrq')))
    return select_sql

def insert_sql(indata):
    """
    插入sql
    """
    if '至' not in str(indata[3]):
        insert_sql = ('insert into T_StockPredict (REPORTCODE,'
                      'STOCKCODE,PERIODDATE,INDATE,PREDICTPRICE'
                      ',msrepl_tran_version)'
                      'values(\'{}\',\'{}\',\'{}\','
                      'getdate(),{},Newid())'.format(
                          indata[0], indata[1], indata[2], indata[3]))
    else:

        min = indata[3].split('至')[0]
        max = indata[3].split('至')[1]
        insert_sql = ('insert into T_StockPredict (REPORTCODE,'
                      'STOCKCODE,PERIODDATE,INDATE,PREDICTMAXPRICE'
                      ',PREDICTMINPRICE,msrepl_tran_version)'
                      'values(\'{}\',\'{}\',\'{}\','
                      'getdate(),{},{},Newid())'.format(
            indata[0], indata[1], indata[2], max,min))


    return insert_sql


def update_sql(indata):
    """
    更新sql
    """
    # print(indata)
    if '至' not in str(indata[3]):
        update_sql = ('update T_StockPredict set INDATE=getdate(),'
                      'PREDICTPRICE={}, PREDICTMAXPRICE={}, PREDICTMINPRICE={}'
                      ' where REPORTCODE=\'{}\' and STOCKCODE = \'{}\''
                      'and PERIODDATE=\'{}\''.format(indata[3],'Null', 'Null',
                                                     indata[0],
                                                     indata[1],
                                                     indata[2]))
    else:

        min = indata[3].split('至')[0]
        max = indata[3].split('至')[1]
        update_sql = ('update T_StockPredict set INDATE=getdate(),'
                      'PREDICTPRICE={},PREDICTMAXPRICE={}, PREDICTMINPRICE={}'
                      ' where REPORTCODE=\'{}\' and STOCKCODE = \'{}\''
                      'and PERIODDATE=\'{}\''.format('Null',max,min,
                                                     indata[0],
                                                     indata[1],
                                                     indata[2]))

    return update_sql
# 查询 的数据库信息
MS = {
    'host': '192.168.1.182',    # 数据库位置
    'user': 'sa',          # 用户名
    'password': 'select*fromvsat',  # 密码
    'db': 'VSATREPORT'         # 数据库名
}


# 数据输出信息
MS1 = {
    'host': '192.168.1.190',    # 数据库位置
    'user': 'sa',          # 用户名
    'password': 'select*fromvsat',  # 密码
    'db': 'VSATREPORT'         # 数据库名
}

# 数据输出信息
# MS1 = {
#     'host': '127.0.0.1',    # 数据库位置
#     'user': 'root',          # 用户名
#     'password': '123456',  # 密码
#     'db': 'vsatTemp'         # 数据库名
# }

conn = pymssql.connect(host=MS.get('host'),
                               user=MS.get('user'),
                               password=MS.get('password'),
                               database=MS.get('db'),
                               charset="utf8")
cour = conn.cursor()
conn1 = pymssql.connect(host=MS1.get('host'),
                        user=MS1.get('user'),
                        password=MS1.get('password'),
                        database=MS1.get('db'),
                        charset="utf8")
cour1 = conn1.cursor()



ws = pd.read_excel('data/20161226lh.xlsx', 0)
#  成功数据集数据集
all_data = {}
# 没有找到 研究报告编码 的记录
error0_list = []
# 有多条研究报告编码的 记录
error1_list = []


#　数据操作结果
insert_list = []
# 更新
update_list = []
# 失败
deal_error_list = []
# 通过数据连接，获得获得  研究报告编码（T_ReportFellow）
# 数据 日志log

log_data = {'debug': 0,
            'error0': 0,
            'error1': 0}

# 添加一个flag  以免因为链接时间过长导致程序失败
flag = 0

# 研究报告编码（T_ReportFellow）
for x in range(len(ws)):
# for x in range(30):
    if flag == 300:
        conn.close()
        conn1.close()
        conn = pymssql.connect(host=MS.get('host'),
                               user=MS.get('user'),
                               password=MS.get('password'),
                               database=MS.get('db'),
                               charset="utf8")
        cour = conn.cursor()
        conn1 = pymssql.connect(host=MS1.get('host'),
                                user=MS1.get('user'),
                                password=MS1.get('password'),
                                database=MS1.get('db'),
                                charset="utf8")
        cour1 = conn1.cursor()
        print('重新链接')
        flag = 1

    else:
        flag += 1
        prim_key = dict(ws.iloc[x, [0, 1, 3, 4]])
        sql_str = get_select(prim_key)

        cour.execute(sql_str)
        select_result = cour.fetchall()
        
        one_item = dict(ws.iloc[x])

        if len(select_result) == 1:
            # 查询研究报告编码
            log_data['debug'] += 1
            print('{code} {name} 查询成功 '.format(code=one_item.get('code'),
                                               name=one_item.get('research')))

            yjbgbm = select_result[0][0]

            all_data[select_result[0][0]] = one_item  # TODO
            
            '''
            开始需要修改
            2016E主营业务收入(万元)
            2016E市盈率
            2016E归属于母公司净利润(万元)
            2016E每股收益
            '''
            # 进行更新的数据
            indata = [
                yjbgbm,
                one_item.get('code'),
                '2016-12-31',
                one_item.get(
                    'mbjw')]
            # print(indata)

            # 判断是否插入还是更新
            select1 = (
                'select * from  T_StockPredict where REPORTCODE='
                ' \'{}\' and STOCKCODE=\'{}\' and PERIODDATE=\'{}\''.format(
                    yjbgbm, indata[1], '2016-12-31'))
            cour1.execute(select1)
            jieguo1 = cour1.fetchall()
            # print(jieguo1)
            if len(jieguo1) == 1:

                print(
                    '{code} {year} {name} 需要更新 '.format(
                        code=one_item.get('code'),
                        year='2016',
                        name=one_item.get('research')))
                update_list.append(indata)
                upd_sql = update_sql(indata)
                if upd_sql ==None:
                    continue
                else:
                    # print(upd_sql)
                    try:
                        cour1.execute(upd_sql)
                        conn1.commit()
                    except Exception as e:
                        print(e)
                        conn1.rollback()
                #
            elif len(jieguo1) == 0:
                print(
                    '{code} {year} {name} 需要插入 '.format(
                        code=one_item.get('code'),
                        year=2016,
                        name=one_item.get('research')))
                insert_list.append(indata)
                ins_sql = insert_sql(indata)
                if ins_sql==None:
                    continue
                else:
                    # print(ins_sql)
                    try:
                        cour1.execute(ins_sql)
                        conn1.commit()
                    except Exception as e:
                        print(e)
                        conn1.rollback()

            else:
                print(
                    '{code} {year} {name} 存在多个报告编码 '.format(
                        code=one_item.get('code'),
                        year='2016',
                        name=one_item.get('research')))
                deal_error_list.append(indata)

        elif len(select_result) == 0:
            log_data['error0'] += 1
            print('{code} {name} 数据查询为0'.format(code=one_item.get('code'),
                                                name=one_item.get('research')))
            error0_list.append(one_item)
        else:
            log_data['error1'] += 1
            error1_list.append(one_item)
            print(
                '{code} {name} 数据有多条记录'.format(
                    code=one_item.get('code'),
                    name=one_item.get('research')))



# 输出程序结果
print('查询研究报告成功次数: {}'.format(len(all_data)))
print('查询研究报告记录为0: {}'.format(log_data['error0']))
print('查询研究报告记录矛盾: {} \n'.format(log_data['error1']))

print('数据更新次数: {}'.format(len(update_list)))
print('数据插入次数: {}'.format(len(insert_list)))
print('数据操作失败次数: {}'.format(len(deal_error_list)))

df_deal_error = pd.DataFrame(deal_error_list)       # 导出库 存在多个报告编码
df_error1 = pd.DataFrame(error1_list)               # 查询 多条记录
df_error0 = pd.DataFrame(error0_list)               # 找不到记录

writer = ExcelWriter('data/mbjerror.xlsx')

df_deal_error.to_excel(writer, '导出出错记录', index=False)
df_error1.to_excel(writer, '多个编码', index=False)
df_error0.to_excel(writer, '没有编码', index=False)
writer.save()


