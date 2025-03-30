from itertools import combinations as cb

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    for i in cb(nums, 3):
        result = sum(i)
        if is_prime(result):
            answer += 1 
                
    return answer