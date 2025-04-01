def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    
    for i in d:
        sum += i

    if sum <= budget:
        answer = len(d)
    else:
        while sum > budget:
            sum = sum - d[-1]
            d.pop()
        answer = len(d)
    return answer