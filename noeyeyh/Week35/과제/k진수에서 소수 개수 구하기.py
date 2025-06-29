# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# k진수로 변환하는 함수
def change_num(n, k):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % k) + result
        n //= k
    return result

def solution(n, k):
    base_k = change_num(n, k)
    # 0을 기준으로 숫자들을 분리
    candidates = base_k.split('0')
    
    count = 0
    for num in candidates:
        if num == '':
            continue
        if is_prime(int(num)):
            count += 1
    return count
