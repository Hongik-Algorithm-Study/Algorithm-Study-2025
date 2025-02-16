from collections import deque

def diff(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count 

def solution(begin, target, words):
    q = deque([[begin, 0]])
    visited = [False] * len(words)

    while q:
        word, dist = q.popleft()
        
        if word == target:
            return dist
            
        for i in range(len(words)):
            if diff(word, words[i]) == 1 and not visited[i]:
                q.append([words[i], dist + 1])
                visited[i] = True     
        
    return 0
