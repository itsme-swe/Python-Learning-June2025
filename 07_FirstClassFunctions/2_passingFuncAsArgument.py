def msg(name):
    return f"Hello, {name}!"


def fun1(fun2, name):
    return fun2(name)


print(fun1(msg, "Harsh"))  # Hello, Harsh!
