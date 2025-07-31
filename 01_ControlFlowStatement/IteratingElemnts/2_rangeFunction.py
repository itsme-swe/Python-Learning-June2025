# The Python range() function returns a sequence of numbers, in a given range. The most common use of it is to iterate sequences on a sequence of numbers using Python loops.

for i in range(1, 11):

    print(i, end=" ")

# 1 2 3 4 5 6 7 8 9 10

print()

arr = [2, 4, 6, 8, 10]

for i in range(len(arr)):
    print(arr[i], end=" ")

# 2 4 6 8 10

print()

# ◽ Iterating over matrix

mtrx = [[2, 4, 6], [1, 3, 5], [7, 8, 9]]

for i in range(len(mtrx)):
    for j in range(len(mtrx[i])):
        print(mtrx[i][j], end=" ")
    print()

"""
2 4 6      
1 3 5      
7 8 9
"""
