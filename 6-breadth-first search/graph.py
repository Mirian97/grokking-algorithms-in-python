from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def is_person_and_mango_seller(name: str):
  return name[-1] == 'm'

def search_in_friends(name: str):
  search_queue = deque()
  search_queue += [name]
  # to avoid looping in search
  verifieds = set()

  while search_queue:
    person = search_queue.popleft()

    if person in verifieds:
      continue
    
    if is_person_and_mango_seller(person):
      print(person + " is a mango seller!")
      return True
    
    search_queue +=graph[person]
    verifieds.add(person)
  return False
      
print(search_in_friends('claire'))