def topological_sort(graph, vertices):
    in_degree = {v: 0 for v in vertices}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = [v for v in vertices if in_degree[v] == 0]
    top_order = []

    while queue:
        u = queue.pop(0)
        top_order.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return top_order


def longest_path_dag(graph, vertices, start):
    top_order = topological_sort(graph, vertices)

    dist = {v: float('-inf') for v in vertices}
    dist[start] = 0

    for u in top_order:
        if dist[u] != float('-inf'):
            for v in graph[u]:
                if dist[v] < dist[u] + 1:
                    dist[v] = dist[u] + 1

    return dist


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

vertices = ['A', 'B', 'C', 'D']
start = 'A'

longest_paths = longest_path_dag(graph, vertices, start)
print("Longest paths from start:", longest_paths)
