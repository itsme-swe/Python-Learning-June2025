from threading import *
from time import *


class MyData:

    def __init__(self):
        self.data = 0
        self.flag = False
        self.lock = Lock()

    # 🔸 Method will be used by producer
    def put(self, d):
        while self.flag != False:
            pass
        self.lock.acquire()
        self.data = d
        self.flag = True
        self.lock.release()

    # 🔸 Now this method will be used by consumer
    def get(self):
        while self.flag != True:
            pass
        self.lock.acquire()
        x = self.data
        self.flag = False
        self.lock.release()
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
