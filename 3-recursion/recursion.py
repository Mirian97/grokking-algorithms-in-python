def search_for_key_1(main_box):
  pile = main_box.create_pile_to_search()
  
  while pile is not empty:
    box = pile.take_box()
    
    for item in box:
      if item.is_a_box():
        pile.append(item)
      elif item.is_a_key():
        print("I find the key!")
        
def search_for_key_2(box):
  for item in box:
    if item.is_a_box():
      search_for_key_2(item)
    elif item.is_a_key():
      print("I find the key!")
