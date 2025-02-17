from collections import deque

def solution(maps):
    x = [0,1,0,-1]
    y = [1,0,-1,0]
    q = deque()
    q.append([0, 0, 1])
    maps[0][0] = 0 #방문하면 0
    while q:
        c, d, dist = q.popleft()
        if c == len(maps)-1 and d == len(maps[0])-1:
            return dist

        for k in range(4):
            a = x[k] + c
            b = y[k] + d
            if 0 <= a < len(maps) and 0 <= b < len(maps[0]) and maps[a][b] == 1:
                q.append([a,b,dist+1])
                maps[a][b] = 0
    return -1