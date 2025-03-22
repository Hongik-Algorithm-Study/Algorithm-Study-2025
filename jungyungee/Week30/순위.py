def solution(n, results):
    rank = []
    for i in range(len(results)):
        if (results[i][0] > results[i][1]):
            rank.append(results[i][0])
    print(rank)
    answer = 0
    return answer