# 💥 find() method in Python returns the index of the first occurrence of a substring within a given string. If the substring is not found, it returns -1.

# 💥 index() method in Python is used to find the position of a specified substring within a given string. It is similar to the find() method but raises a ValueError if the substring is not found, while find() returns -1.

s1 = "Welcome to the tech world"

sFind = s1.find("tech")

sFind1 = s1.find("Tech")


print(sFind)  # 15 is the index value

print(sFind1)  # -1 bcoz Tech is not present

sFind2 = s1.index("Tech")  # ValueError: substring not found
