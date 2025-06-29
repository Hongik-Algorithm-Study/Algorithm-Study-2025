# 소수 판별 알고리즘 - 에라토스테네스의 체 
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    x = []
    
    # k 진수로 바꾸기
    while n > 0 :
        m = n % k
        x.append(m)
        n = n // k
    x.reverse()
    
    # 수 0 기준으로 자르기
    new = ''.join(map(str, x))
    parts = new.split('0')
    
    # 소수 개수 세기
    count = 0
    for i in parts:
        if i and is_prime(int(i)):
            count += 1
    
    return count