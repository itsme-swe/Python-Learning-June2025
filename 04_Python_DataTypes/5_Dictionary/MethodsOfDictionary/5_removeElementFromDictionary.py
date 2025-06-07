# 💥 pop() method removes and returns the value of a specified key from a dictionary. If the key isn't found, you can provide a default value to return instead of raising an error.

d1 = {1: "defender", 2: "land cruiser", 3: "rubicon", 4: "lexus"}

d2 = d1.pop(5, "Not Found")

print(d2)  # Not Found

d3 = d1.pop(3)

print(d3)  # rubicon

print()

# 💥 popitem() method in Python is used to remove and return the last key-value pair from the dictionary. It is often used when we want to remove a random element, particularly when the dictionary is not ordered.