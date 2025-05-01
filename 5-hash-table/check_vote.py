voted = {}

def check_vote(name: str):
  if voted.get(name):
    print("You already voted, bye!")
  else:
    voted[name] = True
    print("Could vote, please")
  
check_vote("tom")
check_vote("mike")
check_vote("mike")