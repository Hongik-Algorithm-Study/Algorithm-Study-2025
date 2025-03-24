from collections import deque

def solution(n, edge):
    # 방문 상태 초기화
    visited = [-1] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    # 그래프 구성
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    # BFS 초기화
    q = deque([1])
    visited[1] = 0
    
    # BFS 탐색
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                q.append(neighbor)
    
    # 최대 거리와 해당 노드 개수 계산
    max_distance = max(visited)
    return visited.count(max_distance)
