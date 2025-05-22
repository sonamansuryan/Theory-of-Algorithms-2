graph = {
    "A": [("B", 4), ("C", 1)],
    "B": [("C", 5), ("D", 2)],
    "C": [("D", 5)],
    "D": [],
}

def dijkstra(graph, start, end):
    distances = {}
    for node in graph:
        distances[node] = float("inf")
    distances[start] = 0

    visited = set()

    while len(visited) < len(graph):
        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None or distances[node] < distances[min_node]:
                    min_node = node
        print(f"Visiting node: {min_node}")
        if distances[min_node] == float('inf'):
            break

        visited.add(min_node)

        for neighbor, weight in graph[min_node]:
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                print(f"Updating distance of {neighbor} to {distances[neighbor]}")

    print(f"Shortest distance from {start} to {end} is {distances[end]}")
    return distances

distances = dijkstra(graph, "A", "D")
