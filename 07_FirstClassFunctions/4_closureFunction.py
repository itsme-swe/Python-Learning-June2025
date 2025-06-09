def Outer():

    msg = "welcome"

    def Inner():
        print("+" * 10)
        print(msg)
        print("+" * 10)

    return Inner


f = Outer()

f()

print()


# 💥 To modify variable of outer function we use nonlocal keyword
def get_counter():

    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


c1 = get_counter()
c2 = get_counter()

print(c1(), c1(), c1())
print(c2(), c2(), c2())
