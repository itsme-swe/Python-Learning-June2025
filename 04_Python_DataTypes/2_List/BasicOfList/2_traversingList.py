l1 = [2, 4, 6, 8, 10]

# 1️⃣ Using for in loop
for ele in l1:
    print(ele, end=" ")

# 2 4 6 8 10

print()

# 2️⃣ Using range() method
l2 = ["Harsh", "Mukul", "Harsh", "Samual"]

for i in range(len(l2)):
    print(l2[i], end=" ")

# Harsh Mukul Harsh Samual

print()

# 3️⃣ Using enumerate()
l3 = ["Harsh", True, l2, 2, 4, 6]

for i, val in enumerate(l3):
    print(f"indexes: {i}, values: {val}")

"""
indexes: 0, values: Harsh
indexes: 1, values: True
indexes: 2, values: ['Harsh', 'Mukul', 'Harsh', 'Samual']
indexes: 3, values: 2
indexes: 4, values: 4
indexes: 5, values: 6
"""

print()

# 4️⃣ list comprehension ⇒ But list comprehension returns new list

l4 = [10, 5, 20, "ajeet", "neha", False]

l5 = [ele for ele in l4]

print(l5)  # [10, 5, 20, 'ajeet', 'neha', False]
