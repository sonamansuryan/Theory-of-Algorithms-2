def bfs(graph, start_node):

    queue = []

    visited = set()

    visit_order = []

    queue.append(start_node)
    visited.add(start_node)

    while queue:
        current_node = queue.pop(0)

        visit_order.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return visit_order

graph = {
    0: [11, 7, 9],
    9: [10, 8],
    7: [11, 6, 3],
    10: [1],
    8: [1, 12],
    6: [5],
    3: [2, 4],
    12: [2],
    11: [],
    5: [],
    2: [],
    4: [],
    1: []
}

result = bfs(graph, 0)
print("BFS այցելման հերթականություն սկսած '0'-ից:", result)