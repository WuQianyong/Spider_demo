#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Time    : 2016/12/30 11:51
# @Author  : wuqianyong
# @File    : email_demo.py
# @Software: PyCharm

"""
使用Python 发送邮件
"""

from email.mime.text import MIMEText

# # 普通邮件
# msg= MIMEText('吴钱勇您好：我是XXX ','plain','utf-8')
# HTML 邮件
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')

# 发送带附件的邮件
from email import encoders
from email.header import Header
from email.mime.multipart import  MIMEMultipart
msg=MIMEMultipart()

fil = '壁纸1.jpg'

msg['Subject'] = '介绍'
msg['From']='Python<wuqianyong1995@163.com>'
msg['To']='小吴同志<1060591592@qq.com>'
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8'))
# 添加一个附件 就是添加一个MIMEBASE 从本地读取一个图片
from email.mime.base import MIMEBase
with open(r'C:\Users\wqy\Pictures\1.jpg', 'rb') as f:
    # print('ok')
    mime = MIMEBase('image','jpg',filename=('gbk', '', fil))
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=('gbk', '', fil))
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # print(mime)
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用Base64 编码
    encoders.encode_base64(mime)
    # print(mime)
    # 添加到attach(mime)
    msg.attach(mime)


print(msg)
# 使用smtplib 发送邮件
user = 'wuqianyong1995@163.com'
password = 'jgsWQY19950105'
smtp_server='smtp.163.com'
to_addr = '1060591592@qq.com'

import smtplib
server = smtplib.SMTP(smtp_server,25) # Smtp协议默认窗口是25
server.set_debuglevel(1)
server.login(user, password)
server.sendmail(user, to_addr, msg.as_string())
server.quit()




