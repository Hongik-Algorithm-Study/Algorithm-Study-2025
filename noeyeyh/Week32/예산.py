def solution(d, budget):
    sum = 0
    count = 0
    d.sort()
    
    for i in d:
        if sum + i > budget:
            break
        sum += i
        count += 1
        
    return count