from itertools import permutations

def is_match(user, banned):
    if len(user) != len(banned):
        return False
    for uc, bc in zip(user, banned):
        if bc != '*' and uc != bc:
            return False
    return True

def solution(user_id, banned_id):
    possible = set()
    for perm in permutations(user_id, len(banned_id)):
        if all(is_match(u, b) for u, b in zip(perm, banned_id)):
            possible.add(frozenset(perm))
    return len(possible)
