states_to_cover = set(["mt", "wa", "or", "id", "nv", "ut","ca","az"]) 

stations = {}
stations["k_first"] = set(["id", "nv", "ut"])
stations["k_two"] = set(["wa", "id", "mt"])
stations["k_three"] = set(["or", "nv", "ca"])
stations["k_four"] = set(["nv", "ut"])
stations["k_five"] = set(["ca", "az"])

def define_states_covereging(states_needed, stations):
  final_stations = set()
  
  while states_needed:
    best_station = None
    covered_states = set()

    for station, states_for_station in stations.items():
      covered = states_needed & states_for_station
      if len(covered) > len(covered_states) and station not in final_stations:
        best_station = station
        covered_states = covered
    
    if best_station is not None:
      states_needed -= covered_states
      final_stations.add(best_station)
      stations.pop(best_station)
  
    else:
      return None
  
  return final_stations

print(define_states_covereging(states_to_cover, stations))