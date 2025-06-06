# 💥 The sort() method in Python is a built-in function that allows us to sort the elements of a list in ascending or descending order and it modifies the list in place which means there is no new list created. This method is useful when working with lists where we need to arranged the elements in a specific order, whether numerically or alphabetically.

l1 = [5, 1, 8, 10, 12, 20, 13]

l1.sort()

print(l1)  # [1, 5, 8, 10, 12, 13, 20]  -- ascending

l2 = [2, 4, 6, 8, 10]

l2.sort(reverse=True)

print(l2)  # [10, 8, 6, 4, 2]  -- descending

print()

# 🔸 Sorting string

# now here we are sorting string on the basis of length
str = ["coat", "python", "black", "cat"]

str.sort(key=len)

print(str)  # ['cat', 'coat', 'black', 'python']
