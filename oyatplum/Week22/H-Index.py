def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i,j in enumerate(citations):
        if (i + 1) <= j:
            answer = i + 1
    return answer