# 💥 We are using predefined locals() method and globals() method to print the respective variables.

x = 10
y = 20


def fun():
    a = 50
    b = 60

    print(locals())
    print(globals())


fun()

# 💥 The function returns output in dictionary form. {'a': 50, 'b': 60}
