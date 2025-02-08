def solution(brown, yellow):
    answer = []
    total = brown + yellow
    temp = []

    for i in range(1, total):
        if total % i == 0:
            temp.append(i)

    for row in temp:
        col = total // row
        exceptVertexCol = col*2 - 4

        if row*2 + exceptVertexCol == brown:
            answer.append(row)
            answer.append(col)
            break

    answer.sort(reverse = True)
    return answer