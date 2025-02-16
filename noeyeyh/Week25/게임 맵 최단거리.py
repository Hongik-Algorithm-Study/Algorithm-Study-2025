from collections import deque

def solution(maps):
    m, n = len(maps), len(maps[0])  # 행과 열의 수
    visited = [[False] * n for _ in range(m)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동 방향
    
    def bfs(start_x, start_y):
        q = deque([(start_x, start_y)])
        visited[start_x][start_y] = True
        maps[start_x][start_y] = 1  # 시작 지점의 거리를 1로 초기화
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1  # 현재 위치에서 1 추가
                    q.append((nx, ny))
    
    bfs(0, 0)
    
    # 도착지점의 값이 1(미로의 끝) 또는 0(도달 불가능)일 경우
    return maps[m-1][n-1] if maps[m-1][n-1] > 1 else -1