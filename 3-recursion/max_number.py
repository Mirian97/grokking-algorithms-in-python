from typing import List

def max_number(arr: List[int]):
  if len(arr) == 2:
    return arr[0] if arr[0] > arr[1] else arr[1]
  
  sub_max = max_number(arr[1:])
  return arr[0] if arr[0] > sub_max else sub_max
    
my_list = [2, 5, 8, 12, 3, 9, 4, 0, 10]
print(max_number(my_list))