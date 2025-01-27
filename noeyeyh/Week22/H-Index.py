def solution(citations):
    citations.sort()
    n = len(citations)

    for h in range(n):
        if citations[h] >= n - h:
            return n - h
        
    return 0