from collections import defaultdict
def solution(genres, plays):
    answer = []
    d1 = defaultdict(list)
    d2 = defaultdict(int)

    for idx, (g, p) in enumerate(zip(genres, plays)):
        d1[g] += [(idx, p)]
        d2[g] += p

    for kind, total in sorted(d2.items(), key = lambda x:x[1], reverse = True):
        for idx, play in sorted(d1[kind], key = lambda x:(-x[1], x[0]))[:2]:
            answer.append(idx)
    return answer