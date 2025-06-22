from collections import deque
def solution(board):
    answer = 0
    N = len(board)
    cost = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)] #초기 비용은 최대로 지정

    dy = [-1, 1, 0, 0]  # 상하좌우
    dx = [0, 0, -1, 1]

    q = deque()

    for d in [1, 3]: #시작점에서 아래(1), 오른쪽(3) 방향으로 출발
        cost[0][0][d] = 0
        q.append((0,0,d,0)) #(x,y,dir,누적비용)을 의미

    while q:
        x,y,dir,c = q.popleft()

        for nd in range(4):
            nx = x + dx[nd]
            ny = y + dy[nd]

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                if dir == nd:
                    nc = c + 100
                else: #방향이 바뀌면 코너임. dir은 이전 방향 nd는 가려는 방향
                    nc = c + 600

                if cost[nx][ny][nd] > nc:
                    cost[nx][ny][nd] = nc
                    q.append((nx, ny, nd, nc))

    return min(cost[N-1][N-1])