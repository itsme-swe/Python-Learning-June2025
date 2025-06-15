from threading import *
from time import *

s = Semaphore(1)


def display(str1):
    s.acquire()
    try:
        for i in str1:
            if i != " ":
                print(f"{current_thread().name}: {i} ")
                sleep(0.4)
    finally:
        s.release()


t1 = Thread(target=display, args=("HELLO WORLD",), name="T1")
t2 = Thread(target=display, args=("Let's connect people",), name="T2")
t3 = Thread(target=display, args=("12345",), name="T3")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
