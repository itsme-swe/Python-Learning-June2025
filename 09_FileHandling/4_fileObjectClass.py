# 💥 The open() function returns an object and here we are seeing the object belongs to which class:

file = open("modeDemo.txt", "r")

print(type(file))  # <class '_io.TextIOWrapper'>

print()

file.close()

# 🔸 Object of binary file:

file1 = open("Binary.txt", "wb")

file1.write("I am binary file created by Harsh\n".encode("utf-8"))
file1.write("I belong to the class known as: \n".encode("utf-8"))


print(type(file1))  # <class '_io.BufferedWriter'>

file1.close()

print()

# 🔸 Properties of object

print(file1.name)  # Binary.txt

print(file1.mode)  # wb

print(file1.closed)  # True
