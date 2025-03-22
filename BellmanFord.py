graph = [
    ['A', 'B', 6],
    ['A', 'C', 4],
    ['B', 'D', 2],
    ['C', 'B', 1],
    ['C', 'D', 3],
    ['C', 'E', 8],
    ['D', 'E', 2]
]

vertex = ['A', 'B', 'C', 'D', 'E']


def Bellman_Ford(graph, vertex, start):
    distance = {}
    previous = {}

    for v in vertex:
        if v == start:
            distance[v] = 0
            previous[v] = None
        else:
            distance[v] = float('infinity')
            previous[v] = None

    for i in range(len(vertex) - 1):
        for u, v, w in graph:
            if distance[u] != float('infinity') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                previous[v] = u

    for u, v, w in graph:
        if distance[u] != float('infinity') and distance[u] + w < distance[v]:
            return "The Graph contains a negative cycle"

    return distance, previous


def get_shortest_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous[current]
    return path


result, previous = Bellman_Ford(graph, vertex, 'A')

if isinstance(result, dict):
    print("Shortest Path from A to E:", get_shortest_path(previous, 'A', 'E'))
else:
    print(result)
