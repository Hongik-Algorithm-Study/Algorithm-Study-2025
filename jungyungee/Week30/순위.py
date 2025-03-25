def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]  #인접 행렬로 그래프 구현
    for a, b in results:
        graph[a][b] = 1

    # 이긴 세력 진 세력 채우기
    fo