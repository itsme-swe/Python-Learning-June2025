# 💥 Defining our own range function


def myRangeFun(n):
    i = 0
    while i < n:
        yield i
        i += 1


for i in myRangeFun(5):
    print(i, end=" ")

# 0 1 2 3 4

print()

# 💥 Printing Days of week using generator


def days():
    d = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    i = 0
    while True:
        yield d[i]
        i = (i + 1) % 7


it = days()

print(next(it))  # sunday
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))  # monday
