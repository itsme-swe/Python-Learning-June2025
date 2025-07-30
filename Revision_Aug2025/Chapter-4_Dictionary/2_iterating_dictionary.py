dict1 = {
    "username": "harsh05",
    "email": "harsh@gmail.com",
    "password": "abc@123",
    "signin-token": "0506",
}

# ◽ Iterate over key-value pairs
for key, val in dict1.items():
    print(f"{key}: {val}")

"""
username: harsh05
email: harsh@gmail.com
password: abc@123
signin-token: 0506
"""

print()

# ◽ Iterate over keys
for key in dict1.keys():
    print(f"{key}")

"""
username
email
password
signin-token
"""
print()

# ◽ Iterate over values
for val in dict1.values():
    print(f"{val}")

"""
harsh05
harsh@gmail.com
abc@123
0506

"""
