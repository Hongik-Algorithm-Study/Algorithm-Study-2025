from itertools import permutations
import math

def solution(numbers):
    def is_prime(x):
        if x < 2:
            return False

        # 2부터 x의 제곱근까지 반복
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False

        return True
    
    permu_list = []
    num_list = list(numbers)
    count = 0
    answer = []
    
    for i in range(len(numbers)):
        temp = list(permutations(num_list, i + 1))
        for j in temp:
            permu_list.append(j)
            
    permu_list = list(set(permu_list))
    
    for i in permu_list:
        if i[0] == '1' and len(i) == 1:
            continue
        if i[0] == '0':
            continue
        answer.append(i)
        
    for i in answer:
        target = ''
        for j in i:
            target += j
            
        target = int(target)
        
        if is_prime(target):
            count += 1
        
    return count