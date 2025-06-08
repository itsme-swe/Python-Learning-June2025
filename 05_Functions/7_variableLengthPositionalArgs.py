def myFun(*args):
    for i in args:
        print(i, end=" ")
    print()


myFun("Hello", "I am", "Harsh", "Mehra")  # Hello I am Harsh Mehra

print()


def displayIntOnly(*args):
    for i in args:
        if type(i) == int:
            print(i, end=" ")


displayIntOnly("harsh", 33, 71.5, True, 15)  # 33 15


# 💥  If we use *args we can pass a variable number of arguments to a function using special symbol.
