l1 = [2, 4, 6]

# 1️⃣ Using append() -- add single element at time

l1.append(8)

print(l1)  # [2, 4, 6, 8]

print()

# 2️⃣ Using extend() -- use to add multiple elements at single time

l1.extend([10, 12, 14, 16])

print(l1)  # [2, 4, 6, 8, 10, 12, 14, 16]

# 3️⃣ Using insert() method to insert element at specific position

l1.insert(2, 50)

print(l1) # [2, 4, 50, 6, 8, 10, 12, 14, 16]
