# 1️⃣ Creating file by using write mode
file = open("modeDemo.txt", "w")

file.write("Hello World Demo\n")
file.write("It's about developers\n")
file.write("Learning Database\n")

file.close()

# 2️⃣ Then reading the data of the file
file1 = open("modeDemo.txt", "r")

data = file1.read()

print(data)

file1.close()

"""
Hello World Demo     
It's about developers
Learning Database 
"""
