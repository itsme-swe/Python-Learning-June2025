s1 = {2, 4, 6, "Movie", True}

for i, val in enumerate(s1):
    print(i, val)

"""
0 True
1 2    
2 Movie
3 4    
4 6 

"""

print()

for i in s1:
    print(i, end=" ")

# True 2 Movie 4 6

print()

# 🔸 Using iter()

for i in iter(s1):
    print(i, end=" ")
