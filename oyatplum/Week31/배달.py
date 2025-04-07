from collections import defaultdict
import heapq

def solution(N, road, K):
    graph = defaultdict(list)
    distance = [float('inf')] * (N+1)
    distance[1] = 0
    heap = [(0,1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist:
            continue
            
        for nxt, cost in graph[now]:
            newDist = dist + cost
            if newDist < distance[nxt]:
                distance[nxt] = newDist
                heapq.heappush(heap, (newDist, nxt))

    return sum(1 for d in distance if d <= K)
