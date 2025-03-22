from collections import deque, defaultdict

def solution(n, edge):
    answer = 0
    q = deque()
    visited = [0] * (n + 1)
    edgeCount = [0] * (n + 1)
    graph = defaultdict(list)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    q.append(1)
    visited[1] = 1

    while q:
        poped = q.popleft()
        for nextNode in graph[poped]:
            if visited[nextNode] == 0:
                visited[nextNode] = 1
                edgeCount[nextNode] = edgeCount[poped] + 1
                q.append(nextNode)

    maxDist = max(edgeCount[1:])
    answer = edgeCount.count(maxDist)

    return answer