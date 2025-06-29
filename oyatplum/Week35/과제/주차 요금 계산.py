from collections import defaultdict, deque
import math
def solution(fees, records):
    answer = []
    tempAn = []
    cars = defaultdict(deque)
    chargeList = []

    for record in records:
        temp = record.split(" ")
        cars[temp[1]].append(temp[0])

    for car in cars:
        if len(cars[car]) % 2 != 0: #개수 홀수면 뒤에 23:59추가
            cars[car].append('23:59')

        totalTime = 0
        totalCharge = 0

        while cars[car]:
            inTime = cars[car].popleft().split(":")
            outTime = cars[car].popleft().split(":")

            hour = int(outTime[0]) - int(inTime[0])
            minutes = int(outTime[1]) - int(inTime[1])

            if minutes < 0: #in minutes가 더 큰 경우
                h = (hour - 1) * 60
                m = (60 - int(inTime[1])) + int(outTime[1])
                totalTime += h + m
            else:
                totalTime += (hour * 60) + minutes

        if totalTime <= fees[0]: #기본 요금만 추가하는 경우
            totalCharge += fees[1]
        else:
            overTime = math.ceil((totalTime - fees[0]) / fees[2]) #올림
            totalCharge += fees[1] + overTime * fees[3] #추가 요금 + 기본 요금

        tempAn.append([car, totalCharge])

    for i in sorted(tempAn, key = lambda x:x[0]):
        answer.append(i[1])

    return answer