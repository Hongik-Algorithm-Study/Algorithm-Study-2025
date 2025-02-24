from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    grid = to_grid(rectangle)
    count = 0
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([([characterX * 2, characterY * 2], count)])

    while queue:
        [x, y], count = queue.popleft()
        if x == itemX * 2 and y == itemY * 2:
            return count // 2

        for mx, my in move:
            if grid[x + mx][y + my] == 1:
                queue.append(([x + mx, y + my], count + 1))


def to_grid(rectangle):
    grid = [[0] * 102] * 102
    for rec in rectangle:
        x1, y1, x2, y2 = [x * 2 for x in rec]

        for x in range(x1, x2 + 1):
            grid[x][y1] = 1
            grid[x][y2] = 1
        for y in range(y1, y2 + 1):
            grid[x1][y] = 1
            grid[x2][y] = 1

    for rec in rectangle:
        x1, y1, x2, y2 = [x * 2 for x in rec]
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                grid[x][y] = 0
    return grid

