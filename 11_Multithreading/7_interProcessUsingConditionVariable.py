# 💥 In this we'll be using Condition Variable and notify() an built-in class provided by threading module instead of lock() and flag.

from threading import *
from time import *


class MyData:

    def __init__(self):
        self.data = 0
        self.cv = Condition()

    def put(self, d):
        self.cv.acquire()
        self.cv.wait(timeout=0)
        self.data = d
        self.cv.notify()
        self.cv.release()
        sleep(0.4)

    def get(self):
        self.cv.acquire()
        self.cv.wait(timeout=0)
        x = self.data
        self.cv.notify()
        self.cv.release()
        sleep(0.4)
        return x


def producer(data):
    i = 1
    while True:
        data.put(i)
        print("producer: ", i)
        sleep(0.8)
        i += 1


def consumer(data):
    while True:
        x = data.get()
        print("Consumer: ", x)
        sleep(0.8)


data = MyData()

t1 = Thread(target=lambda: producer(data))
t2 = Thread(target=lambda: consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()
