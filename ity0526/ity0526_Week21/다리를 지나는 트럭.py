from collections import deque

def solution(bridge_length, weight, truck_weights):
    cur = deque()
    time = 1
    total_weight = 0

    for truck in truck_weights:
        while True:
            if cur and cur[0][1] == time:
                exited_truck = cur.popleft()
                total_weight -= exited_truck[0]

            if total_weight + truck <= weight:
                cur.append((truck, time + bridge_length))
                total_weight += truck
                break
            else:
                if cur:
                    time = cur[0][1]
                else:
                    time += 1

        time += 1

    if cur:
        time = cur[-1][1]

    return time