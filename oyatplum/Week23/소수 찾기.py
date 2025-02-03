from itertools import permutations
def isPrime(target):
    answer = 1
    for i in range(2, target):
        if target % i == 0:
            answer = 0
            return answer
        else:
            continue
    return answer

def solution(numbers):
    answer = 0
    intNumbers = []
    temp = []

    for i in numbers:
        intNumbers.append(i)

    for lenNum in range(len(numbers)):
        for i in permutations(intNumbers, lenNum+1):
            if i in temp:
                continue
            else:
                temp.append(i)

    for i in temp:
        j = "".join(i)
        if j.startswith("0"):
            continue
        elif j == "1":
            continue
        else:
            answer += isPrime(int(j))

    return answer