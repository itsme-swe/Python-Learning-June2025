import time

obj = time.localtime()

print(obj)

# time.struct_time(tm_year=2025, tm_mon=6, tm_mday=16, tm_hour=8, tm_min=2, tm_sec=22, tm_wday=0, tm_yday=167, tm_isdst=0)

print(obj.tm_year)  # 2025
