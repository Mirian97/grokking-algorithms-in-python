def max_steps_by_lenght_list(length: int) -> int:
  steps = 0
  current_length:float = length
  
  while (current_length > 1):
    current_length = current_length /2
    steps+=1
  
  return steps

# max step number to find an item in lenght list
print(max_steps_by_lenght_list(128)) #7
print(max_steps_by_lenght_list(256)) #8