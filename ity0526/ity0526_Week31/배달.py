def solution(N, road, K):
    INF = float('inf')

    roads = [[INF] * (N + 1) for _ in range(N + 1)]

    for a, b, t in road:
        if t < roads[a][b]:
            roads[a][b] = t
            roads[b][a] = t

    time = [INF] * (N + 1)
    check = [False] * (N + 1)

    time[1] = 0

    cur = 1

    for _ in range(N):
        for i in range(1, N + 1):
            if time[cur] + roads[cur][i] < time[i]:
                time[i] = time[cur] + roads[cur][i]

        check[cur] = True

        min_time = INF
        for i in range(1, N + 1):
            if check[i] == False and time[i] < min_time:
                cur = i
                min_time = time[i]

    answer = sum(1 for x in time if x <= K)

    return answer