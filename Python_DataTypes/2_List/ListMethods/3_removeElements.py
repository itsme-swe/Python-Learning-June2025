l1 = [2, 4, 6, 8, 10, 12, 8, 10, 14]

# 1️⃣ Using remove()
l1.remove(8)  # Removes the first occurrence of an element 8.

print(l1)  # [2, 4, 6, 10, 12, 8, 10, 14]

print()

# 2️⃣ Using pop() method --  Removes the element at a specific index or the last element if no index is specified.
l1.pop()

print(l1)  # [2, 4, 6, 10, 12, 8, 10]

l1.pop(5)  # element present at index value 5 will be removed

print(l1)  # [2, 4, 6, 10, 12, 10]

# 3️⃣ Using del statement -- Deletes an element at a specified index.
del l1[1]

print(l1)  # [2, 6, 10, 12, 10]

print()

# 4️⃣ clear() method remove all the elements from the list
l1.clear()

print(l1)  # []
