from typing import List, Optional

def binary_search(arr: List[int], target: int, low: int = 0, high: Optional[int] = None) -> Optional[int]:
  if high is None:
    high = len(arr) -1
    
  if low > high:
    return None
  
  middle = (low + high) // 2
  guess = arr[middle]
  
  if guess == target:
    return middle
  
  elif guess > target:
    return binary_search(arr, target, low, middle -1)
  
  else:
    return binary_search(arr, target, middle + 1, high)

my_list = [4, 5, 8, 10, 11]
print(binary_search(my_list, 8))  # output: 8
print(binary_search(my_list, 11)) # output: 11
print(binary_search(my_list, 7))  # output: None