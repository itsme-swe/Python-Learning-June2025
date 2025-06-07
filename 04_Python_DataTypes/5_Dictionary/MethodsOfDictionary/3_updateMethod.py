# 💥 update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.

d = {1: "Harsh", 2: "Mukul", 3: "Harsh", 4: "James"}

d1 = dict(a=101, b=105, c=201, d=205)

d.update(d1)

print(d)

# {1: 'Harsh', 2: 'Mukul', 3: 'Harsh', 4: 'James', 'a': 101, 'b': 105, 'c': 201, 'd': 205}
