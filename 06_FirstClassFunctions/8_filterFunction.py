# 💥 Creating new list using lambda function but only store multiple of 3

lt = [1, 2, 3, 4, 5, 6, 7, 8, 9]

f = filter(lambda x: x % 3 == 0, lt)

l2 = list(f)

print(l2)  # [3, 6, 9]

print()

# 💥 Now storing only even numbers in list

l3 = filter(lambda x: x % 2 == 0, lt)

print(list(l3))  # [2, 4, 6, 8]

# 💥 filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
