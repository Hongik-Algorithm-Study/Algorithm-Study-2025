from itertools import permutations

def compare(banned, user_id):
    temp = []
    for user in user_id:
        if len(user) != len(banned):
            continue
        else:
            match = True
            for i in range(len(user)):
                if banned[i] == '*':
                    continue
                if banned[i] != user[i]:
                    match = False
                    break
            if match:
                temp.append(user)
    return temp

def solution(user_id, banned_id):
    matched = []

    for b in banned_id:
        matched.append(compare(b, user_id))

    possible = list(permutations(user_id, len(banned_id)))
    result = set()

    for p in possible:
        valid = True
        for i in range(len(banned_id)):
            if p[i] not in matched[i]:
                valid = False
                break
        if valid:
            result.add(tuple(sorted(p)))

    return len(result)