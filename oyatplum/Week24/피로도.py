from itertools import permutations

def solution(k, dungeons):
    answer = -1
    tempAnswer = []
    tempK = k

    for dungeon in permutations(dungeons, len(dungeons)):
        total = 0
        for i in dungeon:
            if i[0] <= tempK:
                tempK -= i[1]
                total += 1
        tempK = k
        tempAnswer.append(total)
    answer = max(tempAnswer)

    return answer