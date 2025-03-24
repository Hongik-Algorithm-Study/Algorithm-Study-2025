def solution(m, n, puddles):
    path = [[0] * m for _ in range(n)]
    puddle_set = {(y-1, x-1) for x, y in puddles}

    for i in range(m):
        if (0, i) in puddle_set:
            break
        path[0][i] = 1

    for i in range(n):
        if (i, 0) in puddle_set:
            break
        path[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if (i, j) in puddle_set:
                path[i][j] = 0
            else:
                path[i][j] = (path[i-1][j] + path[i][j-1]) % 1000000007

    answer = path[n-1][m-1]
    return answer