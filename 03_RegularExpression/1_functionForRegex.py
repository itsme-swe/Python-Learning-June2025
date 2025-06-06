import re

print(re.match("abc", "abcdef"))  # <re.Match object; span=(0, 3), match='abc'>

print(re.fullmatch("python", "python").group())  # python

print(
    re.search("very", "python is very easy language").span()
)  # (10, 14) -- this is returning start and end index values


print(re.findall("can", "can you can a can as a can"))  # ['can', 'can', 'can', 'can']
