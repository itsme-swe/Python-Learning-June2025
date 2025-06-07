d1 = dict(a=101, b=105, c=201, d=205)

# 1️⃣ iterating over keys
for i in d1.keys():
    print(i, end=" ")

# a b c d

print()

# 2️⃣ iterating over values

for i in d1.values():
    print(i, end=" ")

# 101 105 201 205

print()

# 3️⃣ iterating over key value pair

for i, val in d1.items():
    print(f"{i}: {val}", end=" ")

# a: 101 b: 105 c: 201 d: 205
