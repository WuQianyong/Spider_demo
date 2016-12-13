#!/usr/bin/env python
# coding:utf-8
# Build by LandGrey
#

import time
import socket


def readtarget():
    global server_list
    with open(r"servers.txt") as f:
        for line in f.readlines():
            if line[0:1] != "#" and len(line.split(".")) == 4:
                server_list.append(line)


def connserver(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:
        print ("\n 请输入需要更新的部分:\n1.股市日历\n2.发行上市\n3.新股日历\n4.退出")
        data = input()
        if not data:
            break
        if data not in '1234':
            print('输入错误')
            continue
        s.sendall(data.encode())
        print ("Send %s:%s -> %s" % (host, str(connPort), data))
        if data =='4':
            s.close()
            break
        print("程序正在执行中,请稍等")
        time.sleep(0)
        recvdata = s.recv(1024)
        if recvdata.decode()=='OK':
            print ("程序已执行完毕,请查看终端更新情况")


if __name__ == "__main__":
    server_list = []
    connPort = 13800

    readtarget()
    if server_list != []:
        for host in server_list:
            connserver(host, connPort)