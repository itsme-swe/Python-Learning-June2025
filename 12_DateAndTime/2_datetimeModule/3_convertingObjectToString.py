import datetime

x = datetime.datetime(2025, 6, 17, 5, 11, 11)

today = datetime.datetime.now().strftime("%Y,%B %d %I:%M:%S %p")

print(today)  # 2025,June 17 05:21:02 AM
