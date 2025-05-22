def findRedundantConnection(edges):
    parent = [i for i in range(len(edges) + 1)]

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX == rootY:
            return False
        parent[rootY] = rootX
        return True

    for u, v in edges:
        if not union(u, v):
            return [u, v]

n = int(input("Եզրերի քանակը (n): "))
edges = []

print(f"Ներմուծիր {n} եզր, օրինակ՝ '1 2':")
for _ in range(n):
    u, v = map(int, input().split())
    edges.append([u, v])

redundant = findRedundantConnection(edges)
print("Ավելորդ եզր՝", redundant)

