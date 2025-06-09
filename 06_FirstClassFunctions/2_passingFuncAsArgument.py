def msg(name):
    return f"Hello, {name}!"


def fun1(fun2, name):
    return fun2(name)


print(fun1(msg, "Harsh"))  # Hello, Harsh!

print()


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def arithmetic(f, x, y):
    return f(x, y)


sum = arithmetic(add, 10, 30)

print(sum)  # 40
