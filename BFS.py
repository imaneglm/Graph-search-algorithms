from collections import deque

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
Q = deque()
Visited = set()
k_track = {}  # To track the path
path = []   # to save the path 

def BFS(start, goal, graph):
    # Clear previous search data
    Q.clear()
    Visited.clear()
    k_track.clear()
    Q.append(start)
    Visited.add(start)
    k_track[start] = None  # Root has no parent
    path_found = False
    # Continue until queue is empty
    while Q:
        node = Q.popleft()    
        # Check if we found our target node
        if node == goal:
            # Reconstruct the path from goal to start
            current = goal
            while current is not None:
                path.append(current)
                current = k_track[current]
            # Reverse to get path from start to goal
            path.reverse()
            print(f"Shortest path found: {' -> '.join(path)}")
            path_found = True
            break   
        # Explore all neighbors of current node
        for neighbor in graph.get(node, []):
            if neighbor not in Visited:
                Visited.add(neighbor)
                Q.append(neighbor)
                k_track[neighbor] = node  # Save the node it came from 
    # If we didn't find the goal node
    if not path_found:
        print("No such node in the graph")           
# Testing  the BFS function with M,L and K nodes
BFS('A', 'M', graph)
BFS('A', 'L', graph)
BFS('A', 'K', graph)