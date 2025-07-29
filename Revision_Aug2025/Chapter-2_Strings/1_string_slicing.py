num_list = "0123456789"

sliced_str = num_list[
    0:6:2
]  # It means start from idx 0 and move till idx 5 and step after every 2 steps

print(sliced_str)  # 024

# 🔶 A string is a sequence of characters. Python treats anything inside quotes as a string. This includes letters, numbers, and symbols. Python has no character data type so single character is a string of length 1. Strings in Python are immutable. This means that they cannot be changed after they are created. If we need to manipulate strings then we can use methods like concatenation, slicing, or formatting to create new strings based on the original.

# 🔶 Slicing is a way to extract portion of a string by specifying the start and end indexes. The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).

new_list = "246810"

new_slicedList = new_list[:5]  # ◽ Retrieves characters from beginning to index 4

print(new_slicedList)  # 24681

sliced_list = new_list[3:]  # ◽ Retrieves characters from index 3 to the end

print(sliced_list)  # 810

reverse_str = new_list[::-1]  # ◽ Reverse a string

print(reverse_str)  # 018642
