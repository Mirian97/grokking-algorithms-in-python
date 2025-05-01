from typing import List

def quicksort(arr: List[int]):
  if len(arr) < 2:
    return arr
  else:
    pivo = arr[0]
    less_or_equal = [i for i in arr[1:] if i <= pivo]
    greatest = [i for i in arr[1:] if i > pivo]
    return quicksort(less_or_equal) + [pivo] + quicksort(greatest)
  
print(quicksort([10, 5, 2, 3, 12]))