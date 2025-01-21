def solution(distance, rocks, n):
    rocks.sort()
    left = 1
    right = distance
    rocks.append(distance) #마지막 종착점까지 비교해야해서 추가
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        dist = 0
        prev_rock = 0
        delete = 0 #제거한 바위 수

        for rock in rocks:
            dist = rock - prev_rock
            if dist < mid: #간격 mid보다 작다면(거리 최소값 구하니까)
                delete += 1 #바위 제거
                if delete > n: #제거한 바위 수가 n보다 크면 탈출
                    break
            else: #바위 제거하지 않고 prev 갱신
                prev_rock = rock

        if delete > n: #초과해서 제거하면
            right = mid - 1
        else: #이하로 제거하거나 같은 경우
            answer = mid
            left = mid + 1

    return answer