#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

# @Name    : threading_demo
# @Author  : qianyong
# @Time    : 2017-01-17 13:44


"""
多线程
"""
import threading
import time



class MyThread(threading.Thread):  # 继承父类
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting' + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 5)

        print('Exiting' + self.name)

        # 释放锁
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        if exit_flag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1



if __name__ == '__main__':
    exit_flag = 0
    threadLock = threading.Lock()
    threads = []

    # 创建新线程
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)
    thread1.start()
    thread2.start()

    threads.append(thread1)
    threads.append(thread2)

    # 等待所有线程完成
    for t in threads:
        t.join()

    # 开启新线程
    #
    # thread1.join()
    # thread2.join()
    print("退出主线程")
    # import _thread
    # import time
    #
    # # 为线程定义一个函数
    # def print_time( threadName, delay):
    #    count = 0
    #    while count < 5:
    #       time.sleep(delay)
    #       count += 1
    #       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
    #
    # # 创建两个线程
    # try:
    #    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
    #    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
    # except:
    #    print ("Error: 无法启动线程")
    #
    # while 1:
    #    pass
