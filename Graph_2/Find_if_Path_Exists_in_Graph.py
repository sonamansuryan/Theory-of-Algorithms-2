def valid_path(n, edges, source, destination):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        if node == destination:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    return dfs(source)


n = int(input("Ներմուծիր գագաթների քանակը (n): "))
e = int(input("Ներմուծիր եզրերի քանակը: "))
edges = []

print("Ներմուծիր եզրերը (յուրաքանչյուրը՝ օրինակ՝ 0 1):")
for _ in range(e):
    u, v = map(int, input().split())
    edges.append([u, v])

source = int(input("Ներմուծիր սկզբնագագաթը (source): "))
destination = int(input("Ներմուծիր նպատակակետը (destination): "))

result = valid_path(n, edges, source, destination)
print("Արդյունք:", result)
