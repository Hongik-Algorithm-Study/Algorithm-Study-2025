def solution(m, n, puddles):
    puddles = set((puddle[1] - 1, puddle[0] - 1) for puddle in puddles)

    town = [[0] * m for _ in range(n)]

    # 시작점
    town[0][0] = 1

    for i in range(n):
        for j in range(m):
            if (i, j) in puddles:
                town[i][j] = 0
            else:
                if j > 0:
                    town[i][j] += town[i][j - 1]
                if i > 0:
                    town[i][j] += town[i - 1][j]

    return town[n - 1][m - 1] % 1000000007