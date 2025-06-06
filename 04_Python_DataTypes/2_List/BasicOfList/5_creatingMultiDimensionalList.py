l1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6]]

for i in l1:
    print(i, end=" ")

# [1, 2, 3, 4] [5, 6, 7, 8] [9, 8, 7, 6]

print()

for i in range(len(l1)):
    for j in range(len(l1[i])):
        print(l1[i][j], end=" ")
    print()

"""
1 2 3 4 
5 6 7 8
9 8 7 6

"""
