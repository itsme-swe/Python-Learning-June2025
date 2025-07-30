# 🔶 List comprehension is a concise way to create new lists using a single line of code. It is useful for applying an operation or filter to items in an iterable, such as a list or range.

lst = [1, 2, 3, 4, 5, 6, 8]

lst1 = [x * 2 for x in lst]

print(lst1)  # [2, 4, 6, 8, 10, 12, 16]


print()

# Using to extract even numbers from lst
even_num_list = [x for x in lst if x % 2 == 0]

print(even_num_list)  # [2, 4, 6, 8]

print()

# Flattening a nested list

l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

l2 = [num for row in l1 for num in row]

print(l2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ◽ Pro Tip: List comprehension is faster than a for loop in most cases because it’s implemented in C under the hood — great for performance in data-heavy scripts.