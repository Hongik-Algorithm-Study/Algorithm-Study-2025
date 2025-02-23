from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    MAX = 101
    maps = [[0 for _ in range(MAX)] for _ in range(MAX)]
    visited = [[0 for _ in range(MAX)] for _ in range(MAX)]
    
    rectangle = [[x1 * 2, y1 * 2, x2 * 2, y2 * 2] for x1, y1, x2, y2 in rectangle]
    
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2 + 1):
            maps[x][y1] = 1
            maps[x][y2] = 1
        for y in range(y1, y2 + 1):
            maps[x1][y] = 1
            maps[x2][y] = 1

    for x1, y1, x2, y2 in rectangle:
        for i in range(MAX):
            for j in range(MAX):
                if maps[i][j] == 1 and x1 < i < x2 and y1 < j < y2:
                    maps[i][j] = 0

    queue = deque([(characterX*2, characterY*2, 0)])
    
    while queue:
        x, y, c = queue.popleft()
        
        if x == itemX*2 and y == itemY*2: return c//2
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or nx >= MAX or ny < 0 or ny >= MAX or maps[nx][ny] == 0 or visited[nx][ny] == 1:
                continue
            visited[nx][ny] = 1
            queue.append((nx, ny, c + 1))
    
    return -1