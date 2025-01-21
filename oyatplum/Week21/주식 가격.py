from collections import deque

def compare(poped, popedDq):
    time = 0
    for i in popedDq:
        if poped <= i:
            time += 1
        else:
            time += 1
            break
    return time

def solution(prices):
    answer = []
    priceDq = deque()

    for i in prices:
        priceDq.append(i)

    while priceDq:
        poped = priceDq.popleft()
        returnedTime = compare(poped, priceDq)
        answer.append(returnedTime)

    return answer