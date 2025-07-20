def solution(tickets):
    answer = []
    total = len(tickets) + 1

    def dfs(target, route, visited):
        nonlocal total
        if len(route) == total:
            return route

        for idx, ticket in enumerate(tickets):
            if visited[idx] == 0 and ticket[0] == target[1]:
                visited[idx] = 1
                route.append(ticket[1])
                result = dfs(ticket, route, visited)
                if result:
                    return result

    for idx, ticket in enumerate(tickets):
        visited = [0] * len(tickets)

        if ticket[0] == "ICN":
            route = [ticket[0], ticket[1]]
            visited[idx] = 1
            returned = dfs(ticket, route, visited)
            answer.append(returned)

    return sorted(answer)[0]