def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length
    current_weight = 0

    while truck_weights or current_weight > 0:
        current_weight -= q.pop(0)

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                next_truck = truck_weights.pop(0)
                q.append(next_truck)
                current_weight += next_truck
            else:
                q.append(0)
        else:
            q.append(0)

        answer += 1

    return answer