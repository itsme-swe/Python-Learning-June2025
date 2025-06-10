# 💥 Here we'll be handling multiple exceptions in one program

lst = [2, 4, 6, 8, 10]

try:
    idx = 9
    print(lst[idx])
except IndexError as msg:
    print(msg)
except TypeError as msg:
    print(msg)
except:
    print("Some error")

print("End of program")
