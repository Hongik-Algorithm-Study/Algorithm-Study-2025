from collections import defaultdict

def solution(gems):
    total_types = len(set(gems))
    gem_dict = defaultdict(int)

    start, end = 0, 0
    min_length = float('inf')
    answer = [0, 0]

    while end < len(gems):
        gem_dict[gems[end]] += 1
        end += 1

        while len(gem_dict) == total_types:
            if end - start < min_length:
                min_length = end - start
                answer = [start + 1, end]

            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1

    return answer