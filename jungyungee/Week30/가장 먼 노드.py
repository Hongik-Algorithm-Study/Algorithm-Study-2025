def solution(n, edge):
    graph = {}
    for a, b in edge:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append