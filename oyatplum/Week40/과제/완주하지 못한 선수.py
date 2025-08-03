from collections import Counter
def solution(participant, completion):
    answer = ''
    p = Counter(participant)
    c = Counter(completion)

    diff = p - c

    for i in diff:
        answer = i

    return answer