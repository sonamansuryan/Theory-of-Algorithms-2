def calculateMinimumHP(dungeon):
    if not dungeon or not dungeon[0]:
        return 0

    m, n = len(dungeon), len(dungeon[0])
    dp = [[0] * n for _ in range(m)]

    dp[-1][-1] = max(1, 1 - dungeon[-1][-1])

    for j in range(n - 2, -1, -1):
        dp[-1][j] = max(1, dp[-1][j + 1] - dungeon[-1][j])

    for i in range(m - 2, -1, -1):
        dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])

    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            min_hp_on_exit = min(dp[i + 1][j], dp[i][j + 1])
            dp[i][j] = max(1, min_hp_on_exit - dungeon[i][j])

    return dp[0][0]

dungeon = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]

print(calculateMinimumHP(dungeon))