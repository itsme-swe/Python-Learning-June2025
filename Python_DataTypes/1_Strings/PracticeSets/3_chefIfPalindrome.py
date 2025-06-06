str = "madam"

n = len(str)

i = 0
j = n - 1

flag = True

while i < j:
    if str[i] != str[j]:
        flag = False
        break
    i += 1
    j -= 1

if flag:
    print("It's an palindrome")
else:
    print("Not an palindrome")
