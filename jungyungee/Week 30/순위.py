def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]  #인접 행렬로 그래프 구현
    for a, b in results:
        graph[a][b] = 1

    # 이긴 세력 진 세력 채우기
    for k in range(1, n+1): #경유
        for i in range(1, n+1): #출발
            for j in range(n+1): #도착
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph [i][j] = 1

    #이긴 횟수와 진 횟수 각각 저장
    win = {}
    lose = {}
    for i in range(1, n+1):
        win[i] = 0
        lose[i] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j or graph[i][j] == 0:
                pass
            elif graph[i][j] == 1:
                win[i] += 1
            
            if graph[j][i] == 1:
                lose[i] += 1

    answer = 0
    for i in range(1, n+1):
        if win[i] + lose[i] == n-1:
            answer += 1
    return answer

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])