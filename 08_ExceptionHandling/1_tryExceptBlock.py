a = int(input("Enter the value of a: "))

b = int(input("Enter the value of b: "))

try:
    c = a // b
    print(f"Division of a and b is {c}")
except:
    print("b should not be 0")

print("End of program")
