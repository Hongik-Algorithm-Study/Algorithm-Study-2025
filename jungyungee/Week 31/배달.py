import heapq
INF = float('inf')

def solution(N, road, K):
    # 최단거리, 부모 저장 테이블
    path = [[INF, i] for i in range(N+1)]
    path[1] = [0,1]
    
    # 우선순위 큐(힙) -> 이용해 최소거리 찾아냄
    q = [(0,1)]
    while q:
        dist, now = heapq.heappop(q)
        for a, b, value in road:
            if a == now and path[b][0] > value + dist:
                heapq.heappush(q, (dist + value, b))
                path[b] = [value + dist, now]
            elif b == now and path[a][0] > value + dist:
                heapq.heappush(q, (dist + value, a))
                path[a] = [value + dist, now]
    
    answer = 0
    for i in path:
        if i[0] <= K:
            answer += 1
            
    return answer

solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4)