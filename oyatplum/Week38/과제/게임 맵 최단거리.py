from collections import deque
def solution(maps):
    xL = [0, 1, 0, -1]
    yL = [1, 0, -1, 0]

    q = deque()
    q.append([0, 0, 1]) #x, y, 거리
    maps[0][0] = 0 #처음 방문 표시

    while q:
        x, y, dist = q.popleft()

        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return dist

        for i in range(4):
            dx = xL[i] + x
            dy = yL[i] + y

            if 0 <= dx < len(maps) and 0 <= dy < len(maps[0]) and maps[dx][dy] == 1:
                q.append([dx, dy, dist+1])
                maps[dx][dy] = 0 #방문 처리

    return -1