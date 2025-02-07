from itertools import permutations


def solution(k, dungeons):
    all_route = list(permutations(dungeons))
    max_count = 0

    for route in all_route:
        max_count = max(max_count, explore(k, route))

    return max_count


def explore(k, dungeons):
    count = 0
    energy = k

    for d in dungeons:
        if energy >= d[0]:
            energy -= d[1]
            count += 1
        else:
            break

    return count
