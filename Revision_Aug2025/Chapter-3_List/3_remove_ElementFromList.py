# 🔶 remove() function removes the first occurrence of a given item from list. It make changes to the current list. It only takes one argument, element we want to remove and if that element is not present in the list, it gives ValueError.

l1 = [2, 4, 6, 8, 10]
l2 = [1, 3, 5, 6, 7, 9, 10]

for item in l2:
    if item in l1:
        l1.remove(item)

print(l1)  # [2, 4, 8]


# 🔶 pop() method is used to remove an element from a list at a specified index and return that element. If no index is provided, it will remove and return the last element by default.

print(l2.pop())  # 10
