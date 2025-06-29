def solution(n, times):
    answer = 0
    left = 1 #범위가 반환하려는 최소 대기 시간 -> left, right, mid에 해당
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        people = 0 #기준이 사람 수

        for time in times:
            people += mid // time #mid 시간 동안 해당 심사관에게 받는 사람 수
            if people >= n:
                break
        if people >= n :
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer