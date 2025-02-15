def solution(n, computers):
    networks = 0
    visited = [False] * n

    def DFS(com):
        visited[com] = True
        for i in range(n):
            if computers[com][i] == 1 and not visited[i]:
                DFS(i)

    for i in range(n):
        if not visited[i]:
            DFS(i)
            networks += 1

    return networks



