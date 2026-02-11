import heapq 

graph = [
  ('1', '2', 5),
  ('1', '3', 10),
  ('2', '4', 9),
  ('3', '6', 2),
  ('4', '6', 4),
  ('4', '5', 5),
  ('6', '7', 3),
  ('3', '9', 7),
  ('7', '8', 1),
  ('9', '10', 1),
  ('8', '9', 3),
  ('7', '10', 4)
]
VISITED = set()
PQ = [] #Min-Heap is a way to store a tuples (priorities minimal) 
arc_list = {}

def UCS(start, goal, graph):
    # Storing each arc (node it start from , node it get to the weight of arc)
    for u, v, cost in graph:
        if u not in arc_list:
            arc_list[u] = []
        arc_list[u].append((v, cost))
    heapq.heappush(PQ, (0, start, [start]))  # (cost, node, path) 
    while PQ:
        # Pop the lowest cost node
        current_cost, current_node, path = heapq.heappop(PQ)
        if current_node in VISITED:
            continue    #if the node is already visited go to next           
        if current_node == goal:
            return current_cost, path
        VISITED.add(current_node)   # add the node we go throught add to visited set
        for neighbor, arc_cost in arc_list.get(current_node, []):
            if neighbor not in VISITED:
                total_cost = current_cost + arc_cost 
                new_path = path + [neighbor] 
                heapq.heappush(PQ, (total_cost, neighbor, new_path)) 
    return "No path found"

# Testing part
cost, path = UCS('1', '7', graph)
print(f" Path: {' -> '.join(path)}, It's cost: {cost}")