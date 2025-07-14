def solution(n, wires):
    temp = []

    graph = [[] for _ in range(n+1)]

    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    def dfs(start, visited, count):
        count = 1

        for node in graph[start]:
            if visited[node] == 0:
                visited[node] = 1
                count += dfs(node, visited, count)
        return count

    for wire in wires:
        visited1 = [0] * (n+1)
        visited2 = [0] * (n+1)

        visited1[wire[0]] = 1
        visited2[wire[1]] = 1

        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])

        count = 0

        first = dfs(wire[0], visited1, count)
        second = dfs(wire[1], visited2, count)

        temp.append(abs(first - second))

        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    return min(temp)