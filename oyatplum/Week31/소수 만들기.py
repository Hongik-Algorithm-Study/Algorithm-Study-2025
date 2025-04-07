from itertools import combinations
import math

def isPrime(sumNum):
    for i in range(2, int(math.sqrt(sumNum)) + 1):
        if sumNum % i == 0:
            return False
    return True
    
def solution(nums):
    answer = 0
    temp = list(combinations(nums, 3))
    
    for target in temp:
        sumNum = sum(target)
        result = isPrime(sumNum)
        if result:
            answer += 1
                
    return answer
