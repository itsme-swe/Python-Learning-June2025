# 🔶 find() method in Python returns the index of the first occurrence of a substring within a given string. If the substring is not found, it returns -1. This method is case-sensitive, which means "abc" is treated differently from "ABC".

# Syntax - s.find(substring, start, end)) and even we can pass start index and end index also.

trip = "We'll be doing Leh Ladakh Circuit"

find_str = trip.find("Leh")

print(find_str) # 15
