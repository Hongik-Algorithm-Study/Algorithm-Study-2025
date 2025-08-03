from collections import Counter
def solution(participant, completion):
    part = Counter(participant)
    comp = Counter(completion)
    answer = part - comp
    return list(answer.keys())[0]