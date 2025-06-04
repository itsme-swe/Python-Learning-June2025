# enumerate() is a built-in Python function that lets you loop over a sequence (like a list, tuple, or string) and get both the index and the value at the same time.

lst = ["apple", "banana", "orange", "kiwi"]

for i, val in enumerate(lst):
    print(f"index: {i}, value: {val}")

"""
index: 0, value: apple
index: 1, value: banana
index: 2, value: orange
index: 3, value: kiwi

"""
