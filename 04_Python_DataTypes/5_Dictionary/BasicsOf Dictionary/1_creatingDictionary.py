# 💥 Using Literal
d = {1: "Harsh", 2: "Mukul", 3: "Harsh", 4: "James"}

print(d)  # {1: 'Harsh', 2: 'Mukul', 3: 'Harsh', 4: 'James'}

print()

# 💥 Using dict() constructor

d1 = dict(a=101, b=105, c=201, d=205)

print(d1)  # {'a': 101, 'b': 105, 'c': 201, 'd': 205}

print()

# 💥Passing list of tuple to dict() constructor

d2 = dict([(1, "one"), (2, "two"), (3, "three"), (4, "four")])

print(d2)  # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

print()

# 💥 Using enumerate()
l1 = ["defender", "land cruiser", "rubicon", "lexus"]

d3 = dict(enumerate(l1, start=1))

print(d3) # {1: 'defender', 2: 'land cruiser', 3: 'rubicon', 4: 'lexus'}
