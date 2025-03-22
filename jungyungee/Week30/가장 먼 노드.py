def solution(n, edge):
    graph = {}
    for a, b in edge:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a) 

    depth_map = {1: 0}
    queue = [1]
    visited = set([1])

    while queue:
        i = queue[0]
        for next in graph[i]:
            if next not in visited:
                visited.add(next)
                queue.append(next)
                depth_map[next] = depth_map[i]+1
        queue.pop(0)
    max_depth = max(depth_map.values())
    answer = list(depth_map.values()).count(max_depth)
    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])