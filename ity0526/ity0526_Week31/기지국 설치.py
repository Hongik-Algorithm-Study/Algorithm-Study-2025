import math

def solution(n, stations, w):
    answer = 0

    dist = 1 + 2 * w

    left = 1
    right = 0

    for i in stations:
        right = i - w - 1

        if left <= right:
            answer += math.ceil((right - left + 1) / dist)
            left = i + w + 1
        else:
            left = i + w + 1

    if left <= n:
        answer += math.ceil((n - left + 1) / dist)

    return answer