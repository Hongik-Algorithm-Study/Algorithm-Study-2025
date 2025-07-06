from collections import defaultdict
from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []

    infoHash = defaultdict(list)

    for i in info:
        splitedInfo = i.split()
        score = int(splitedInfo.pop())

        for r in range(5): #0부터 4까지 '-'를 몇 개 넣을지 결정
            combs = combinations(range(4), r) #4자리 중 r개 선택

            for comb in combs:
                key = splitedInfo[:]
                for elem in comb:
                    key[elem] = '-' #comb 자리마다 '-'로 대체
                infoHash[''.join(key)].append(score)

    for item in infoHash:
        infoHash[item].sort() #점수 정렬

    for q in query:
        splitedQ = q.replace(" and", " ").split()
        targetScore = int(splitedQ.pop())

        targetKey = ''.join(splitedQ)

        matchedList = infoHash[targetKey] #해당 쿼리에 맞는 점수 리스트

        if not matchedList:
            answer.append(0) #해당 값 없는 경우
            continue

        scoreLen = len(matchedList)

        # upper bound 알고리즘
        start = bisect_left(matchedList, targetScore)

        answer.append(scoreLen - start)

    return answer