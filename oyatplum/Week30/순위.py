from collections import defaultdict, deque
def solution(n, results):
    answer = 0
    upGraph = defaultdict(set)
    downGraph = defaultdict(set)
    countList = [[0]*2 for _ in range(n)]

    for up, down in results:
        upGraph[down].add(up)
        downGraph[up].add(down)

    def bfs(graph, node):
        q = deque()
        q.append(node)
        visited = [0] * (n+1)
        visited[node] = 1

        while q:
            poped = q.popleft()
            for nextNode in graph[poped]:
                if visited[nextNode] == 0:
                    visited[nextNode] = 1
                    q.append(nextNode)
                    graph[node].add(nextNode)

    for node in range(1, n+1):
        bfs(upGraph, node)
        bfs(downGraph, node)

    for node in upGraph:
        countList[node-1][0] = len(upGraph[node])

    for node in downGraph:
        countList[node-1][1] = len(downGraph[node])

    for node in countList:
        if node[0] + node[1] == n-1:
            answer += 1

    return answer