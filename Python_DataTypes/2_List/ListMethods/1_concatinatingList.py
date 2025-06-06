l1 = [2, 4, 6]

l2 = [1, 3, 5]

l3 = l1 + l2

print(l3)  # [2, 4, 6, 1, 3, 5]

print()

# 1️⃣ Using extend() method

l1.extend(l2)

print(l1)  # [2, 4, 6, 1, 3, 5]

print()

# 2️⃣ Using * operator
lt1 = ["Harsh", "Mukul", "John"]

lt2 = [2, 4, 6]

lt3 = [*lt1, *lt2]  # # Using the unpacking operator to merge the lists

print(lt3)  # ['Harsh', 'Mukul', 'John', 2, 4, 6]
