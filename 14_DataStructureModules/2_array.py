# 💥 Array is like list only but the difference is the array module stores only homogenous types and list stores hetrogenous types.

import array

arr = array.array("i", [10, 20, 30, 40, 50])

for i in range(len(arr)):
    print(arr[i], end=" ")

# 10 20 30 40 50
