# 💥 map() function is used to apply a given function to every item of an iterable, such as a list or tuple, and returns a map object (which is an iterator).

# 1️⃣ # This function is simply doubles the provided number


def double(x):
    return x * 2


l1 = [1, 2, 3, 4]

l2 = list(map(double, l1))

print(l2)  # [2, 4, 6, 8]

print()

# 2️⃣ Using lambda expression

l3 = list(map(lambda x: x * 2, l2))

print(l3)  # [4, 8, 12, 16]

print()

# 3️⃣ Using condition in lambda function -- convert all odd numbers into -ve

lt = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lt1 = list(map(lambda x: x if x % 2 == 0 else -x, lt))

print(lt1)  # [-1, 2, -3, 4, -5, 6, -7, 8, -9]
