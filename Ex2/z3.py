def binary_search(array, low, high, i):
    if high >= low:
        half = (high + low) // 2
        if array[half] == i:
            return array[half]
        elif array[half] > i:
            return binary_search(array, low, half - 1, i)
        else:
            return binary_search(array, half + 1, high, i)
 
    else:
        return -1

arr = [1,2,3,4,5]
res = binary_search(arr, 0, len(arr) -1, -2)
if res != -1:
  print("Found")
else:
  print("Not in list")