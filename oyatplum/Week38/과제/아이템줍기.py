from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    count = 0

    dotList = []
    x = [0, 1, 0, -1]
    y = [1, 0, -1, 0]

    visited = [[0] * 102 for _ in range(102)]

    q = deque()

    for rect in rectangle:
        for tempX in range(rect[0]*2, rect[2]*2+1):
            dotList.append([tempX, rect[1]*2]) #아랫변
            dotList.append([tempX, rect[3]*2]) #윗변
        for tempY in range(rect[1]*2, rect[3]*2+1):
            dotList.append([rect[0]*2, tempY]) #좌변
            dotList.append([rect[2]*2, tempY]) #우변

    q.append([characterX*2, characterY*2])

    while q:
        for _ in range(len(q)):
            popedX, popedY = q.popleft()
            visited[popedX][popedY] = 1 #방문

            if popedX == itemX*2 and popedY == itemY*2:
                return count // 2

            for i in range(4):
                nextX = popedX + x[i]
                nextY = popedY + y[i]

                skip = False

                for rect in rectangle:
                    if nextX in range(rect[0]*2+1, rect[2]*2) and nextY in range(rect[1]*2+1, rect[3]*2):
                        skip = True
                        break
                if skip:
                    continue

                if [nextX, nextY] in dotList and visited[nextX][nextY] == 0:
                    q.append([nextX, nextY])
        count += 1

    return -1