from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        poped = q.popleft()
        temp = 0
        for i in q:
            if poped <= i:
                temp += 1
            else:
                temp += 1
                break
        answer.append(temp)

    return answer