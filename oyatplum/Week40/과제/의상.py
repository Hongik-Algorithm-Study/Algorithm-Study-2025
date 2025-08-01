from collections import defaultdict
def solution(clothes):
    answer = 1
    d = defaultdict(list)

    for cloth in clothes:
        d[cloth[1]].append(cloth[0])

    if len(d) > 1:
        for c in d:
            answer *= (len(d[c]) + 1)
        return answer - 1
    else:
        for c in d:
            return len(d[c])