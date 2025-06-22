from collections import defaultdict

def solution(gems):
    gem_types = set(gems)         # 보석 종류들
    gem_dict = defaultdict(int)   # 현재 구간의 보석 개수
    total_types = len(gem_types)  # 필요한 보석 종류 수

    answer = [0, len(gems)-1]     # 최악의 경우 전체 구간
    left = 0

    for right in range(len(gems)):
        gem_dict[gems[right]] += 1

        while len(gem_dict) == total_types:
            # 구간 최소면 갱신
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            
            gem_dict[gems[left]] -= 1
            if gem_dict[gems[left]] == 0:
                del gem_dict[gems[left]]
            left += 1

    return [answer[0]+1, answer[1]+1]
