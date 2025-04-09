def dungeon(grid):
    rows, cols = len(grid), len(grid[0])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    start, end = None, None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    if not start or not end:
        return "Something is wrong with the grid"

    queue = [(start[0], start[1], 0)]
    visited = set([start])

    while queue:
        x, y, steps = queue.pop(0)

        if (x, y) == end:
            return f"Escape is possible: time {steps} minutes"

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] in ('.', 'E') and (nx, ny) not in visited:
                    queue.append((nx, ny, steps + 1))
                    visited.add((nx, ny))

    return "Escape is impossible"

dungeon_example = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'E', '.', '#', '.']
]

print(dungeon(dungeon_example))
