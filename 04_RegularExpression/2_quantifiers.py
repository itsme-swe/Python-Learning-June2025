import re

print(re.fullmatch("(ab)?", "ab").group())  # ab

print(re.fullmatch("(ab)*", "ababababab").span())  # (0, 10)

print(re.findall("[abc]+", "123 abc 987 bbcc@cbac"))  # ['abc', 'bbcc', 'cbac']
