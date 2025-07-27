from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()

    for idx, p in enumerate(priorities):
        q.append((idx, p))

    maxNum = max(q, key = lambda x:x[1])[1]

    while q:
        popedIdx, popedVal = q.popleft()
        if popedIdx != location:
            if popedVal != maxNum:
                q.append((popedIdx, popedVal))
            else:
                maxNum = max(q, key = lambda x:x[1])[1]
                answer += 1
        else:
            if popedVal != maxNum:
                q.append((popedIdx, popedVal))
            else:
                answer += 1
                break

    return answer