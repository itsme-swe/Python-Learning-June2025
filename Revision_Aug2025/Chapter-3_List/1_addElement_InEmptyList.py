# 🔶 append() method in Python is used to add a single item to the end of list. This method modifies the original list and does not return a new list.
lst = []

lst.append("Chandigarh")
lst.append("Manali")

print(lst)  # ['Chandigarh', 'Manali']

print()

# extend() method is used to add items from one list to the end of another list. This method modifies the original list by appending all items from the given iterable.

# Using extend() method is easy and efficient way to merge two lists or add multiple elements at once.

lst1 = ["Sissu", "Sarchu", "Leh"]

lst.extend(lst1)

print(lst)  # ['Chandigarh', 'Manali', 'Sissu', 'Sarchu', 'Leh']
