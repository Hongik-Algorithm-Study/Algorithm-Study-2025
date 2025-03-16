def solution(m, n, puddles):
    dp = [[-1] * (m + 1) for _ in range(n + 1)]

    for i in range(m + 1):
        dp[0][i] = 0
    for i in range(n + 1):
        dp[i][0] = 0
    for p in puddles:
        i, j = p[0], p[1]
        dp[j][i] = 0

    dp[0][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] != 0:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m] % 1000000007