cardNum = input("Enter the 12 digit card number: ")

lastDigit = cardNum[8:]

fourX = ("X" * 4) + " "

displayCardNum = (fourX * 2) + lastDigit

print(f"Your card number is {displayCardNum}")

# Your card number is XXXX XXXX 5615
