def fun(a, b, c, /, d):
    print(a, b, c, d)


fun(10, 20, 30, d=40)  # 10 20 30 40

fun(40, 50, 60, 70)  # 40 50 60 70

fun(10, 20, c=30, d=50)
# ◽ This will throw an error bcoz we are passing keyword argument also and the function will accept only positional argument bcoz of './'
