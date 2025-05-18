from collections import deque

def solution(board):
    N = len(board)
    INF = float('inf')
    visited = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    q = deque()

    for d in range(4):
        visited[0][0][d] = 0

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상
    q.append((0, 0, -1, 0))

    while q:
        y, x, prev_d, cost = q.popleft()

        for d in range(4):
            ny, nx = y + dirs[d][0], x + dirs[d][1]

            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                new_cost = cost + 100 if prev_d == -1 or prev_d == d else cost + 600

                if visited[ny][nx][d] > new_cost:
                    visited[ny][nx][d] = new_cost
                    q.append((ny, nx, d, new_cost))

    return min(visited[N-1][N-1])