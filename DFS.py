graph = {
  'A': ['B', 'G'],
  'B': ['C', 'D'],
  'C': ['E'],
  'D': ['F'],
  'E': [],
  'F': ['L'],
  'G': ['H'],
  'H': ['F', 'I'],
  'I': ['J', 'K'],
  'J': ['L'],
  'K': [],
  'L': []
}
S = []  
Visited = set()
#1 recursive method  function to apply the DFS .
def dfs_recursive(graph, node, Visited):
    if node not in Visited:
        Visited.add(node)  
        print(f"{node}")
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, Visited) 
print("Visited node order for recursive method:")
 #Starting the function from A the root node.
dfs_recursive(graph, 'A', Visited)

# 2 DFS method (iterative DFS using a stack)
def DFS(graph, start, goal):
    Visited.clear()   # using same set from the previous function
    S.append(start)
    Visited.add(start)
    print("Order of visited nodes of the DFS: ")
    while S:
        node = S.pop()
        print(f"{node}") 
        if node == goal:
            return "Goal Found"
        #  to start researching from left to right (standard or most comman way of expanding the nodes) reverse the graph
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in Visited:
                Visited.add(neighbor)
                S.append(neighbor)
    return "Goal Not Found"
print(DFS(graph, 'A', 'K'))