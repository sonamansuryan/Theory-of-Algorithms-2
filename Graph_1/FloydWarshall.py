INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)

    dist = [row[:] for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

graph = [
    [0,   3, INF, 7],
    [8, 0,  2, INF],
    [5, INF,   0, 1],
    [2, INF, INF, 0]
]

shortest_paths = floyd_warshall(graph)

print("Կարճագույն ուղիների մատրիցը՝")
for row in shortest_paths:
    print(row)
