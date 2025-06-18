from collections import Counter

l1 = ["Mark", "Jhonny", "David", "Mark", "David"]

c = Counter(l1)

print(c)

# Counter({'Mark': 2, 'David': 2, 'Jhonny': 1})

c.update({"Juhu": 3})

print(c)
# Counter({'Juhu': 3, 'Mark': 2, 'David': 2, 'Jhonny': 1})


for i in c.elements():
    print(i, end=" ")

# Mark Mark Jhonny David David Juhu Juhu Juhu