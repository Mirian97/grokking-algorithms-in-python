from typing import List

def sum(arr: List[int]) -> int:
  if len(arr) == 0:
    return 0
  else: 
    return arr[0] + sum(arr[1:])

my_list = [4, 5, 8, 3]
print(sum(my_list))