from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque(truck_weights)
    totalWeight = 0 #다리 위 트럭 총 무게
    ing = deque([0] * bridge_length) #건너는 트럭

    while totalWeight > 0 or q: #처음 트럭이 올라가기 전에 시작해야해서, q에 트럭 모두 사라지고 ing에 트럭 모두 건널 때까지
        time += 1
        popedIng = ing.popleft() #건너는 트럭 한칸씩 앞으로
        totalWeight -= popedIng

        if q:
            if totalWeight + q[0] <= weight: #다음 트럭 올라갈 수 있으면
                popedTruck = q.popleft()
                ing.append(popedTruck)
                totalWeight += popedTruck
            else:
                ing.append(0)
        else:
            ing.append(0)

    return time