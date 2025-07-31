num = int(input("Enter the value of n: "))

res = "Even" if num % 2 == 0 else "Odd"

print(res)

print()

# Using Tuple

output = ("Odd", "Even")[num % 2 == 0]

print(output)
