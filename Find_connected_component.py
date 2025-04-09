def dfs(graph, node, visited, component):
    visited.add(node)
    component.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)


def find_connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)

    return components

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3],
    5: []
}

components = find_connected_components(graph)
print("Connected Components:", components)
