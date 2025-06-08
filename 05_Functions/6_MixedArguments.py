# 💥 Here we will be writing function which will accept both positional and keyword arguments.


def fun(a, b, /, *, c, d):
    print(a, b, c, d)


fun("Harsh", "Mukul", c=33, d=32) # Harsh Mukul 33 32
