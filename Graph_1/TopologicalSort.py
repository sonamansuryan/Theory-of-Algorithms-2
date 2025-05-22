graph = {
    "G": ["B", "F"],
    "B": ["C", "F"],
    "C": ["D"],
    "F": ["D", "E"],
    "A": ["B", "C"],
    "D": [],
    "E": []
}

def dfs(graph, vertex, stack, visited):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, stack, visited)
    stack.append(vertex)

def topological_sort(graph):
    stack = []
    visited = set()

    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, stack, visited)

    ordering = []
    while stack:
        ordering.append(stack.pop())

    return ordering

result = topological_sort(graph)
print("Topological Sort-ը՝", result)
