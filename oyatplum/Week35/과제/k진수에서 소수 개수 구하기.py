import math
def solution(n, k):
    answer = 0

    def change(n, k): #진수 변환
        reN = ''
        while n > 0:
            mod = n % k
            n = n // k
            reN += str(mod)
        return reN[::-1]

    changedN = change(n, k)
    changedList = changedN.split("0")

    def isPrime(n): #소수 판별
        if n < 2:
            return 0
        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return 0
            return 1

    for i in changedList:
        if len(i) > 0: #공백인 경우 필터링
            answer += isPrime(int(i))

    return answer