import heapq
from collections import defaultdict

def solution(N, road, K):
    graph = defaultdict(list)
    
    # 그래프 구성
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 거리 초기화
    distance = [float('inf')] * (N + 1)
    distance[1] = 0
    
    # 우선순위 큐 초기화
    pq = [(0, 1)]  # (거리, 노드)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # 현재 노드까지의 거리보다 더 긴 경우 무시
        if current_distance > distance[current_node]:
            continue

        # 이웃 노드 탐색
        for neighbor, weight in graph[current_node]:
            distance_via_current = current_distance + weight
            
            # 최단 거리 갱신
            if distance_via_current < distance[neighbor]:
                distance[neighbor] = distance_via_current
                heapq.heappush(pq, (distance_via_current, neighbor))

    # K 이하의 거리 카운트
    answer = sum(1 for d in distance if d <= K)
    
    return answer
