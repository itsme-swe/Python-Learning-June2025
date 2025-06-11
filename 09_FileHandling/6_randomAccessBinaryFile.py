# 💥 To close the file automatically use with keyword while opening the file

with open("binaryRead.txt", "wb") as bf:
    bf.write("abcdefgh".encode("utf-8"))

with open("binaryRead.txt", "rb") as data:
    print(data.read(2).decode("utf-8"))  # ab
    data.seek(4, 1)  # g
    print(data.read(1).decode("utf-8"))


""" 💥
0 ⇒ Move from starting point of file  
1 ⇒ Move from current position
2 ⇒ Move from end of the file
"""
