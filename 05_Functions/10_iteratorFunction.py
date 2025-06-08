l1 = ["harsh", 32, "fair", 71.5, False]

it = iter(l1)

print(next(it))  # harsh
print(next(it))  # 32
print(next(it))  # fair

print()

# 💥 Using while loop to iterate list using iter()

while True:
    try:
        print(next(it), end=" ")

    except StopIteration:
        print("End of Loop")
        break

# harsh 32 fair 71.5 False End of Loop
