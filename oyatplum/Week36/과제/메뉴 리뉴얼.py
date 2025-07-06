from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu in orders:
            for li in combinations(menu, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sortedCandidates = Counter(candidates).most_common() #개수로 내림차순
        if sortedCandidates:
            maxCount = sortedCandidates[0][1]
            for menu, count in sortedCandidates:
                if count > 1 and count == maxCount:
                    answer.append(menu)
    return sorted(answer)