def solution(m, n, puddles):
    path = [[0] * m for _ in range(n)]
    for i in puddles:
        path[i[0]][i[1]] = 0

    for i in range(m):
        path[0][i] = 1
    for i in range(n):
        path[i][0] = 1

    for i in range(1,m):
        for j in range(1,n):
            if (i==int(puddles[0][0])-1 and j==int(puddles[0][1])-1):
                path[i][j]=0
            else:
                path[i][j] = path[i][j-1]+path[i-1][j]

    answer= path[m][n]
    return answer

solution(4, 3, [[2,2]])