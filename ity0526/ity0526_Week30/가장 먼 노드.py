from collections import deque

def solution(n, edge):

    graph = [[] for _ in range(n+1)]

    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    distance = [-1] * (n+1)
    distance[1] = 0
    queue = deque([1])

    while queue:
        cur_node = queue.popleft()
        for i in graph[cur_node]:
            if distance[i] == -1:
                distance[i] = distance[cur_node] + 1
                queue.append(i)

    max_dist = max(distance)
    return distance.count(max_dist)