from typing import List

def count_list_itens(arr: List[int]):
  if arr == []:
    return 0
  else:
    return 1 + count_list_itens(arr[1:])
  
my_list = [4, 5, 8, 3, 9, 4, 0, 10]
print(count_list_itens(my_list))