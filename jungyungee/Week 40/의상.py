def solution(clothes):
    from collections import defaultdict
    hash_map = defaultdict(int)

    for name, kind in clothes:
        hash_map[kind] += 1

    result = 1
    for count in hash_map.values():
        result *= (count + 1)

    return result - 1