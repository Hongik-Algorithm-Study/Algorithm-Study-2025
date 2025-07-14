from itertools import permutations
import math
def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numList = []

    for n in numbers:
        numList.append(n)

    primeTest = set()

    for i in range(1, len(numList) + 1):
        numTemp = set(permutations(numList, i))
        for temp in numTemp:
            target = ''
            for t in temp:
                target += t
            primeTest.add(int(target))

    for test in primeTest:
        if test == 0 or test == 1:
            continue
        else:
            if isPrime(test):
                answer += 1

    return answer