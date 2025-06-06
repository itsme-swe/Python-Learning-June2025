import datetime

# 💥 Using f-string (formatted string literals) to simplify string formatting and interpolation.
name = "Harsh"
age = 32

print(f"My name is {name} and I am {age} years old.")

# My name is Harsh and I am 32 years old.

print()

# 💥 Printing date and time using f-string
today = datetime.datetime.today()

print(f"{today: %B %d, %Y}")  # June 04, 2025
