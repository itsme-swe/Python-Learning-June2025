add = lambda x, y: x + y

print(add(50, 50))

print()

# 💥 Without assigning to any variable

print((lambda x: x * 2)(5))  # 10

print()

# 💥 Creating new list using lambda function but only store multiple of 3

lt = [1, 2, 3, 4, 5, 6, 7, 8, 9]

f = filter(lambda x: x % 3 == 0, lt)

l2 = list(f)

print(l2) # [3, 6, 9]