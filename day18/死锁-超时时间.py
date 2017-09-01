# -*- coding:utf-8 -*-

'给死锁设置超时时间'

__author__ = '建磊'

from threading import Thread
from threading import Lock
import time

def main():

    def fn1():
        if lock1.acquire():
            print('fn1中的lock1上锁成功')
            time.sleep(1)
            lock2.acquire(timeout=3)
            print('fn1中的lock2上锁成功')
            lock2.release()
        lock1.release()

    def fn2():
        if lock2.acquire():
            print('fn2中的lock2上锁成功')
            time.sleep(1)
            lock1.acquire(timeout=3)
            print('fn2中的lock1上锁成功')
            lock1.release()
        lock2.release()

    lock1 = Lock()
    lock2 = Lock()
    th1 = Thread(target=fn1)
    th2 = Thread(target=fn2)
    th1.start()
    th2.start()

if __name__ == '__main__':
    main()
