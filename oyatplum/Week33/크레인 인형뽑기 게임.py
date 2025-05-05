from collections import deque
def solution(board, moves):
    answer = 0
    q = deque()
    stack = []

    for m in moves:
        q.append(m)

    while q:
        poped = q.popleft() - 1
        for idxR, row in enumerate(board):
            flag = False #루프 탈출 위한 플래그
            for idxC, col in enumerate(row):
                if poped == idxC: #moves와 열 같은 경우
                    if col == 0:
                        continue
                    else:
                        if stack:
                            a = stack.pop()
                            if a == col:
                                answer += 2
                            else:
                                stack.append(a)
                                stack.append(col) #스택에 추가
                        else:
                            stack.append(col) #스택에 추가
                        board[idxR][idxC] = 0 #board 0으로 초기화
                        flag = True #루프 탈출 위한 플래그
            if flag:
                break

    return answer