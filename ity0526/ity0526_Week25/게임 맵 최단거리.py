from collections import deque

def solution(maps):
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([(0, 0, 1)])

    n, m = len(maps), len(maps[0])

    while queue:
        x, y, distance = queue.popleft()

        if x == n-1 and y == m-1:
            return distance

        for mx, my in move:
            next_x, next_y = x + mx, y + my
            if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] == 1 :
                maps[next_x][next_y] = 0
                queue.append((next_x, next_y, distance + 1))

    return -1
