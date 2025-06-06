# 💥 List slicing is fundamental concept that let us easily access specific elements in a list. We can use both positive and negative indexing for slicing.

# 1️⃣ Get elements from index 1 to 4 (excluded)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:4])  # [2, 3, 4]

print()

# 2️⃣ Get all elements in the list
print(a[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print()

# 3️⃣  Printing all elements from starting to index 5
print(a[:5])  # [1, 2, 3, 4, 5]

print()

# 4️⃣ Print elements from index 5 to last of list
print(a[5:])  # [6, 7, 8, 9]

print()

#5️⃣ Get every second element from the list starting from the beginning
print(a[::2]) # [1, 3, 5, 7, 9]
