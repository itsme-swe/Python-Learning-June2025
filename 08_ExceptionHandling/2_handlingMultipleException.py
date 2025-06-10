# 💥 Here we'll be handling multiple exceptions in one program

lst = [2, 4, 6, 8, 10]

try:
    idx = 2
    print(lst[idx])
except (IndexError, TypeError) as msg:
    print(msg)
except:
    print("Some error")

print("End of program")
