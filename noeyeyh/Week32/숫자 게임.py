def solution(A, B):
    A.sort()
    B.sort()
    count = 0
    j = 0
    
    for a in A:
        while j < len(B):
            if B[j] > a:
                count += 1
                j += 1
                break
            j += 1
            
    return count
