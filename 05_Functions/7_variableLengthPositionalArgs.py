def myFun(*args):
    for i in args:
        print(i, end=" ")
    print()


myFun("Hello", "I am", "Harsh", "Mehra")  # Hello I am Harsh Mehra

# 💥  If we use *args we can pass a variable number of arguments to a function using special symbol.
