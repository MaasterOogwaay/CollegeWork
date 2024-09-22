from threading import *
import time
import sys

Res = 0
lock = Lock()


def main():
    global Res
    t1 = Thread(target=step1)
    t2 = Thread(target=step2)
    t2.start()
    t1.start()
    t1.join()
    t2.join()
    print('Final Value: ', Res)


def step1():
    global Res, lock
    lock.acquire()
    localVal1 = Res
    for i in range(1, 101):
        localVal1 += 1
        time.sleep(0.02)
    Res = localVal1
    lock.release()


def step2():
    global Res, lock
    lock.acquire()
    localVal2 = Res
    for i in range(1, 101):
        localVal2 += 2
        time.sleep(0.02)
    Res = localVal2
    lock.release()


main()
