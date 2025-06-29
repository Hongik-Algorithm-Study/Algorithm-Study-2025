def solution(A, B):
    answer = 0
    a_sorted = sorted(A, reverse=True)
    b_sorted = sorted(B, reverse=True)
    
    for i in range(len(A)-1):
        if b_sorted[i] > a_sorted[i]:
            answer += 1
        else:
            last = b_sorted[-1]
            del b_sorted[-1]
            b_sorted.insert(0, last)

    if b_sorted[-1] > a_sorted[-1]:
        answer += 1
    
    return answer