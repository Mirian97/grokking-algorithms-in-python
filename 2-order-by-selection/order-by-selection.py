from typing import List

def search_small_number(arr: List[int]):
  small = arr[0]
  small_index = 0
  
  for i in range(1, len(arr)):
    if(arr[i] < small):
      small = arr[i]
      small_index = i
      
  return small_index

def order_by_selection(arr: List[int]):
  new_array = []
  
  for i in range(len(arr)):
    small = search_small_number(arr)
    new_array.append(arr.pop(small))
    
  return new_array

my_array = [5, 4, 3, 6, 2, 10]

# O(n²)
print(order_by_selection(my_array))
    