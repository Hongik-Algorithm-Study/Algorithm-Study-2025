from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    turn = 0
    q = deque()
    q.append(begin)
    visited = [begin]

    while q:
        for _ in range(len(q)): #bfs 한 단계마다 turn 증가
            poped = q.popleft()
            for word in words:
                diff = 0
                if word not in visited:
                    for i, j in zip(poped, word):
                        if i != j:
                            diff += 1
                    if diff == 1:
                        if word == target:
                            return turn + 1
                        else:
                            visited.append(word)
                            q.append(word)
        turn += 1
    return 0