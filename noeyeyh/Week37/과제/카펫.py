def solution(brown, yellow):
    total = brown + yellow
    answer = []
    
    #가로는 a 세로는 b
    for b in range(1, total + 1):
        if total % b == 0: 
            a = total // b
            
            if 2 * (a + b) - 4 == brown:
                answer = [a, b] 
                break

    return answer