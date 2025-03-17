def solution(m, n, puddles):
    gridList = [[0] * m for _ in range(n)]
    gridList[0][0] = 1  # 시작점

    for x,y in puddles: #웅덩이 체크
        gridList[y - 1][x - 1] = -1  # 웅덩이는 -1로 표시

    for row in range(n):
        for col in range(m):
            if gridList[row][col] == -1:
                gridList[row][col] = 0
                continue

            if col > 0:
                gridList[row][col] += gridList[row][col - 1]

            if row > 0:
                gridList[row][col] += gridList[row - 1][col]

            gridList[row][col] %= 1000000007

    return gridList[n-1][m-1]