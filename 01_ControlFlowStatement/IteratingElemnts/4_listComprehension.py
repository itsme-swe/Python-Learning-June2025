# List comprehension is a way to create lists using a concise syntax. It allows us to generate a new list by applying an expression to each item in an existing iterable (such as a list or range).

# 1️⃣ We have a list of integers and want to create a new list containing the square of each element, we can easily achieve this using list comprehension.
arr = [2, 4, 6, 8]

sqArr = [eachVal**2 for eachVal in arr]

print(sqArr, end=" ")  # [4, 16, 36, 64]

print()

# 2️⃣ Extract vowels from a string

str = "Welcome to the jungle"

vowelArr = [eachCh for eachCh in str if eachCh in "aeiouAEIOU"]

print("vowelArr: ", vowelArr, end=" ")

# vowelArr:  ['e', 'o', 'e', 'o', 'e', 'u', 'e']