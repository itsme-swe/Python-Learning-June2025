from threading import *
from time import *


def display(str1):
    for x in str1:
        print(x)
        sleep(0.5)


t1 = Thread(target=display, args=("HELLO WORLD",))

t2 = Thread(target=display, args=(" You are welcome",))

t1.start()
t2.start()

t1.join()
t2.join()

"""
💥 Example of Race condition without proper synchronisation.

A race condition occurs when two or more threads (or processes) access the same shared resource (e.g., a variable or function) concurrently, and at least one thread modifies it, without proper synchronization, causing unpredictable or mixed results based on timing.
"""
