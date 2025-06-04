item = str(input("Enter the name of dish: "))

price = input("Enter the price of dish: ")

dash = 20 - len(item) - len(price)

print(item + ("-" * dash) + price)

# Burger-----------100