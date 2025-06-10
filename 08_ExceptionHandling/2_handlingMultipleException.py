# 💥 Here we'll be handling multiple exceptions in one program

lst = [2, 4, 6, 8, 10]

try:
    idx = 6
    print(lst[idx])
except IndexError:
    print("Invalid Index")
except TypeError:
    print("Index should be integer")
except:
    print("Some error")

print("End of program")

