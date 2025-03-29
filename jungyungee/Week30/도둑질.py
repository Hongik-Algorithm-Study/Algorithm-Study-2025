def solution(money):
    #두 가지 경우: 맨 앞의 것 선택 (마지막 선택 불가) or 마지막 것 선택(맨 앞의 것 선택 불가)
    n = len(money)

    # 맨 앞의 것 선택
    case1 = money[0:n-1]
    dp1 = [0] * len(case1)
    for i in range(len(case1)):
        if i == 0:
            dp1[i] = case1[i]
        elif i == 1:
            dp1[i] = max(case1[0], case1[1])
        else:
            dp1[i] = max(dp1[i-1], dp1[i-2] + case1[i])
    result1 = dp1[-1]
    
    # 맨 뒤의 것 선택
    case2 = money[1:n]
    dp2 = [0] * len(case2)
    for i in range(len(case2)):
        if i == 0:
            dp2[i] = case2[i]
        elif i == 1:
            dp2[i] = max(case2[0], case2[1])
        else:
            dp2[i] = max(dp2[i-1], dp2[i-2] + case2[i])
    result2 = dp2[-1]

    answer = max(result1, result2)
    return answer

solution([1, 3, 4, 1, 2, 4, 1, 3, 2])