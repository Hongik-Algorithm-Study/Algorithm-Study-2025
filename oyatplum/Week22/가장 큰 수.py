def solution(numbers):
    answer = ''
    strNumbers = list(map(str, numbers))
    strNumbers.sort(key = lambda x:x*3, reverse = True)

    for i in strNumbers:
        answer += i

    return str(int(answer))