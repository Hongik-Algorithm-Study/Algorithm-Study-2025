def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(i+1):
            if (j==0):
                triangle[i][j] += triangle[i-1][0]
            elif (i == j):
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    answer =  max(map(max, triangle))
    return answer

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])