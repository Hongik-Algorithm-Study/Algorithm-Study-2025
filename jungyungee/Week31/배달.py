import heapq
MAX = 2000

def solution(N, road, K):
    # 최단거리, 부모 저장 테이블
    path = [[MAX, i] for i in range(N+1)]
    #path[1] = [0,1]
    
    # 우선순위 큐(힙) -> 이용해 최소거리 찾아냄
    q = [(0,1)]
    while q:
        dist, now = heapq.heappop(q)
        for a, b, value in road:
            if a == now and path[now][0] > value + dist:
                heapq.heappush(q, (value, b))
                path[b] = [value + dist, now]
            elif b == now and path[now][0] > value + dist:
                heapq.heappush(q, (value, a))
                path[a] = [value + dist, now]
 