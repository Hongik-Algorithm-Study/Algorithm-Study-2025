from collections import deque

def solution(priorities, location):
    answer = 1
    queue = deque()

    for i,j in enumerate(priorities):
        queue.append((i,j))

    maxNum = max(queue, key=lambda x:x[1])[1]

    while queue:
        poped = queue.popleft()
        if poped[1] < maxNum:
            queue.append(poped)
            continue
        else:
            if poped[0] == location:
                break
            else:
                answer += 1
                maxNum = max(queue, key=lambda x:x[1])[1]
                continue
        break

    return answer