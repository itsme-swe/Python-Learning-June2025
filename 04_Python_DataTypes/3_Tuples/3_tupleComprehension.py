tup1 = (*(x for x in range(1, 5)),)

print(tup1)  # (1, 2, 3, 4)

print()

# 💥 Alternative way to perform same tuple comprehension

tup2 = tuple(x for x in range(1, 6))

print(tup2) # (1, 2, 3, 4, 5)
