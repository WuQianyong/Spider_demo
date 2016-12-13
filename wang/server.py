#!/usr/bin/env python
# coding:utf-8
# Build by LandGrey
#

import time
import socket
import threading
import os



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('0.0.0.0', 13800))
s.listen(5)
print('Waiting for connection...')


# def parsecmd(strings):
#     midsplit = str(strings).split(" ")
#     if len(midsplit) >= 2 and midsplit[0] == "cmd":
#         try:
#             command = subprocess.Popen(strings[4:], shell=True)
#             command.communicate()
#             print ("\n")
#         except Exception as e:
#             print (e.message)
#             traceback.print_exc()

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    # sock.send(b'command received')
    while True:
        print ("Connect success -> %s at %s \n" % (str(sock), time.strftime("%Y%m%d %H:%M:%S", time.localtime())))
        if sock:
            while True:
                data = sock.recv(1024)
                if data.decode() =='1':
                    print ("Receive:%s" % data.decode())
                    os.chdir('E:\\执行程序\\股市日历\\股市日历(仿wind)')
                    start=os.popen('StockCalendar.exe')
                    time.sleep(30)
                    stop=os.system('taskkill /F /IM StockCalendar.exe')
                    sock.sendall('OK'.encode())
                if data.decode() =='2':
                    print ("Receive:%s" % data.decode())
                    os.chdir('E:\\执行程序\\首页页面\\首叶最新')
                    start=os.popen('HomePageHtml.exe')
                    time.sleep(15)
                    stop=os.system('taskkill /F /IM HomePageHtml.exe')
                    sock.sendall('OK'.encode())
                if data.decode() =='3':
                    print ("Receive:%s" % data.decode())
                    os.chdir('E:\\执行程序\\新股日历\\最新修改')
                    start=os.popen('NewStockCalenderN.exe')
                    time.sleep(150)
                    stop=os.system('taskkill /F /IM NewStockCalenderN.exe')
                    sock.sendall('OK'.encode())
                # if data.decode() =='4':
                #     print ("Receive:%s" % data.decode())
                #     sock.sendall('[Server]success'.encode())
                #     start=os.popen('E:\\常用\\AdbeRdr1012_en_US.exe')
                #     time.sleep(10)
                #     stop=os.system('taskkill /F /IM msiexec.exe')
                # if data.decode() =='5':
                #     print ("Receive:%s" % data.decode())
                #     sock.sendall('[Server]success'.encode())
                #     start=os.popen('E:\\常用\\360sd_se_3.0.0.3031L.exe')
                #     time.sleep(10)
                #     stop=os.system('taskkill /F /IM 360sd_se_3.0.0.3031L.exe')
                if data.decode() =='4':
                    print ("Receive:%s" % data.decode())
                    sock.close()
                    break

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

