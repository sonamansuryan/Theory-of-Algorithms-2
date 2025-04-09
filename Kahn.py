def kahn_topological_sort(graph):
    in_degree = {}
    for u in graph:
        if u not in in_degree:
            in_degree[u] = 0
        for v in graph[u]:
            if v not in in_degree:
                in_degree[v] = 0
            in_degree[v] += 1

    queue = []
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    top_order = []

    while queue:
        node = queue.pop(0)
        top_order.append(node)

        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(top_order) != len(in_degree):
        print("Սխալ. Գրաֆում կա ցիկլ։")
        return []

    return top_order

graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

result = kahn_topological_sort(graph)
print("Թոփոլոգիական դասավորություն:", result)