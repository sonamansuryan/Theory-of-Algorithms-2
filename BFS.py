def bfs(graph, start_node):
    """
        Implements Breadth-First Search (BFS) algorithm on a graph

        Parameters:
        graph: dictionary where keys are nodes and values are lists of adjacent nodes
        start_node: starting node for the search

        Returns:
        list of visited nodes in BFS order
    """

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
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C'],
    'E': ['C', 'F'],
    'F': ['E']
}

result = bfs(graph, 'A')
print("BFS այցելման հերթականություն սկսած 'A'-ից:", result)