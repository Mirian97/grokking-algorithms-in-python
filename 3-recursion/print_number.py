def print_number(number: int):
  print(number)
  # base case
  if number <= 1:
    return
  # recursive case
  else:
    print_number(number - 1)
  
print_number(30)