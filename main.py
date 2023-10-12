def hill_climbing(graph, start_node):
    current_node = start_node
    path = [current_node]

    while True:
        neighbors = graph.get(current_node, {})
        if not neighbors:
            break
        best_neighbor = max(neighbors, key=neighbors.get)
        if neighbors[best_neighbor] <= neighbors.get(current_node, 0):
            break
        current_node = best_neighbor
        path.append(current_node)

    return path


graph_data = {
    'A': {'B': 5, 'C': 3, 'U': 4},
    'B': {'E': 2, 'G': 3},
    'C': {'G': 3, 'I': 6, 'J': 4},
    'U': {'K': 1, 'Y': 2},
    'E': {'G': 3, 'M': 0},
    'G': {'M': 0},
    'I': {'M': 0},
    'J': {'K': 1},
    'K': {'J': 2},
    'Y': {'M': 0},
    'M': {}

}


start_node = 'A'
path = hill_climbing(graph_data, start_node)

print("Path:", " -> ".join(path))


