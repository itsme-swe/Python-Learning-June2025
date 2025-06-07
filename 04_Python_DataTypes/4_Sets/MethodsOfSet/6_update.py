# 💥 update() method add multiple elements to a set. It allows you to modify the set in place by adding elements from an iterable (like a list, tuple, dictionary, or another set).

s1 = {1, 2, 3}

s1.update([3, 4, 5])

print(s1)  # {1, 2, 3, 4, 5}

s1.update((5, 6, 7))

print(s1)  # {1, 2, 3, 4, 5, 6, 7}

