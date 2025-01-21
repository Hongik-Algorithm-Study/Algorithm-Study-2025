from collections import deque

def solution(prices):
    p_stack = deque()
    answer = [0] * len(prices)

    for index, price in enumerate(prices):
        while p_stack and p_stack[-1][0] > price:
            last_price, last_index = p_stack.pop()
            answer[last_index] = index - last_index
        p_stack.append((price, index))

    while p_stack:
        last_price, last_index = p_stack.pop()
        answer[last_index] = len(prices) - last_index - 1

    return answer