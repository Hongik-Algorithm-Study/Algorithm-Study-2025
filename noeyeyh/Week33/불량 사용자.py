from itertools import permutations

def check(user, ban):
    if len(user) != len(ban):
        return False
    for i, j in zip(user, ban):
        if j == '*':
            continue
        if i != j:
            return False
    return True

def solution(user_id, banned_id):
    answer = set()

    for i in permutations(user_id, len(banned_id)):
        if all(check(a, b) for a, b in zip(i, banned_id)):
            answer.add(frozenset(i))  # 순서와 상관없이 동일한 조합이면 중복 제거

    return len(answer)