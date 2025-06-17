# 💥 Find the month which is starting from monday

import datetime

year = int(input("Enter the year: "))

monday = 0

for month in range(1, 13):
    dt = datetime.date(year, month, 1)

    if dt.weekday() == 0:
        monday += 1
        print(month)

print(f"Number of months starting from Monday = {monday}")
