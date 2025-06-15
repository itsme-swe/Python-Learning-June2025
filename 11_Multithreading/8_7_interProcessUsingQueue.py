from threading import *
from time import *
from queue import *

# Create a thread-safe Queue which acts as a message queue between producer and consumer
q = Queue()

# Function for the producer thread
def producer(que):
    i = 1
    while True:
        que.put(i)
        print("producer: ", i)
        sleep(0.8)
        i += 1

# Function for the consumer thread
def consumer(que):
    while True:
        x = que.get()
        print("Consumer: ", x)
        sleep(0.8)


t1 = Thread(target=lambda: producer(q))
t2 = Thread(target=lambda: consumer(q))

t1.start()
t2.start()

t1.join()
t2.join()
