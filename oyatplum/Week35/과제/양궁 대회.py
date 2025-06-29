def solution(n, info):
    answer = [-1]
    maxDiff = 0

    def dfs(idx, arrows, lion, peach, board):
        nonlocal answer, maxDiff

        if arrows > n: #다 쏜 경우 리턴
            return

        if idx == 11: #마지막까지 오면
            board[10] += n - arrows #남은 화살 0점에 몰아넣기
            diff = lion - peach #라이언과 어피치 점수 차이

            if diff > 0:
                if diff > maxDiff:
                    maxDiff = diff
                    answer = board[:]
                elif diff == maxDiff: #낮은 점수 많이 맞힌 경우 우선
                    for i in reversed(range(11)):
                        if board[i] > answer[i]:
                            answer = board[:]
                            break
                        elif board[i] < answer[i]:
                            break
            return

        #이기는 경우 -> 어피치 + 1
        take = info[idx] + 1
        if arrows + take <= n:
            newBoard = board[:]
            newBoard[idx] = take #라이언 배열 갱신
            dfs(idx + 1, arrows + take, lion + (10 - idx), peach, newBoard)

        #지는 경우 -> 0으로
        newBoard = board[:]
        if info[idx] > 0: #어피치가 해당 점수 맞춘 경우
            dfs(idx+ 1, arrows, lion, peach + (10- idx), newBoard)
        else: #어피치도 못 쏜 경우
            dfs(idx+ 1, arrows, lion, peach, newBoard)

    dfs(0, 0, 0, 0, [0]*11)

    return answer