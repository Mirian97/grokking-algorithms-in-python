infinite = float("inf")

graph = {}
graph["voce"] = ["alice", "bob", "claire"]
graph["inicio"] = {}
graph["inicio"]["a"] = 6
graph["inicio"]["b"] = 2
graph["a"] = {}
graph["a"]["fim"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fim"] = 5
graph["fim"] = {}

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fim"] = infinite

parents = {}
parents["a"] = "inicio"
parents["b"] = "inicio"
parents["fim"] = None
processeds = []

def find_the_lowest_cost(custos):
  lowest_cost = float("inf")
  lowest_cost_node = None
  
  for node in custos:
    cost = custos[node]
    if cost < lowest_cost and node not in processeds:
      lowest_cost = cost 
      lowest_cost_node = node
  
  return lowest_cost_node

node = find_the_lowest_cost(costs)

while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  
  for n in neighbors.keys(): 
    new_cost = cost + neighbors[n]
    if costs[n] > new_cost: 
      costs[n] = new_cost 
      parents[n] = node
      
  processeds.append(node) 
  node = find_the_lowest_cost(costs)
    
print("Cost from the start to each node:")
print(costs)