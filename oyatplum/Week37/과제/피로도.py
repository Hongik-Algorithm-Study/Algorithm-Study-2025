from itertools import permutations
def solution(k, dungeons):
    answer = -1
    permutes = list(permutations(dungeons, len(dungeons)))

    for perm in permutes:
        cur = k
        total = 0
        for p in perm:
            if cur >= p[0] and cur - p[1] >= 0:
                cur -= p[1]
                total += 1
        if total > answer:
            answer = total

    return answer