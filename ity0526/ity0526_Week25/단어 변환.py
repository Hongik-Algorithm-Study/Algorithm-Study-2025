from collections import deque


def solution(begin, target, words):
    queue = deque([(begin, 0)])
    visited = set()
    while queue:
        start, count = queue.popleft()

        for word in words:
            if word not in visited and can_change(start, word):
                if word == target:
                    return count + 1

                visited.add(word)
                queue.append((word, count + 1))

    return 0


def can_change(start, word):
    one_different = False

    for s, w in zip(start, word):
        if not one_different:
            if s != w:
                one_different = True
        else:
            if s != w:
                return False

    return True