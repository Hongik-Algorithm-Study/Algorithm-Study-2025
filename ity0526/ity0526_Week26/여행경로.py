from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)

    route = []

    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        route.append(airport)

    dfs("ICN")

    return route[::-1]
