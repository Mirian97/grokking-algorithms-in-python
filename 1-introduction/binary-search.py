from typing import List, Optional

def binary_search( numberList: List[int], target: int ) -> Optional[int]:
  low = 0
  high = len(numberList) - 1
  
  while (low <= high):
    middle = (low + high) // 2
    guess =  numberList[middle]
    
    # If the index equal to target
    if(guess == target):
      return middle
    
    # The guess is too high
    if(guess > target):
      high = middle - 1
    
    # The guess is too low
    else:
      low = middle +1
    
  return None

myList = [5, 6, 7, 10, 15, 16, 19]
print(binary_search(myList, 8))
print(binary_search(myList, 15))