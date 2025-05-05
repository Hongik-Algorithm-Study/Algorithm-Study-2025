def solution(board, moves):
    basket = []
    removed = 0

    for move in moves:
        col = move - 1

        # 해당 열에서 인형 찾기
        for row in range(len(board)):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0

                if basket and basket[-1] == doll:
                    basket.pop()
                    removed += 2
                else:
                    basket.append(doll)
                break

    return removed