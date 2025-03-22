graph = {
    0: [9],
    1: [0],
    2: [],
    3: [2, 4, 5],
    4: [],
    5: [6],
    6: [7],
    7: [3, 10],
    8: [1, 7],
    9: [8],
    10: [11],
    11: [7],
    12: []
}

visited = set()


def dfs(graph, node, visited, parent=None):
    if node not in visited:
        visited.add(node)
        print(f"Այցելվում է հանգույց՝ {node}:")

        is_dead_end = True
        for neighbor in graph[node]:
            if neighbor not in visited:
                is_dead_end = False
                dfs(graph, neighbor, visited, node)

        if len(graph[node]) == 0:
            print(f"Հանգույց {node}-ը տերև է:")

        elif is_dead_end and parent is not None:
            print(f"Հանգույց {node}-ը փակուղի է:")


dfs(graph, 0, visited)
