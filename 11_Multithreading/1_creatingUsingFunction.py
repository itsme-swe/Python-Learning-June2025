# 💥 Here we are creating multithread program using function
from threading import *
from time import *


def display():
    for i in range(65, 91):
        print(chr(i))
        sleep(1)


# 🔸 obj of thread
t = Thread(target=display, name="Alphabets")

t.start()

for i in range(65, 91):
    print(i)
    sleep(1)

t.join()
