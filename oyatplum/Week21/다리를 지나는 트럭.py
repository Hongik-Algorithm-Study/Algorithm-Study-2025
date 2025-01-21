from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    watitingDq = deque()
    goingDq = deque()

    for i in truck_weights:
        watitingDq.append(i)

    goingWeight = 0 #다리에 있는 트럭 무게

    while len(watitingDq) != 0:
        poped = watitingDq.popleft() #대기에서 제거
        if len(goingDq) < bridge_length: #시간 비교
            if goingWeight + poped <= weight: #무게 비교
                goingWeight += poped #다리에 트럭 무게 추가
                goingDq.append(poped) #다리 트럭 배열에 추가
                time += 1
            else:
                goingDq.append(0)
                time += 1
                watitingDq.appendleft(poped)

        elif len(goingDq) == bridge_length:
            gogingPoped = goingDq.popleft() #다리에서 트럭 제거
            goingWeight -= gogingPoped #다리에서 트럭 무게 제거
            watitingDq.appendleft(poped)

    return time + bridge_length