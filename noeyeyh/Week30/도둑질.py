def solution(money):
    def rob_linear(houses):
        n = len(houses)
        if n == 0:
            return 0
        if n == 1:
            return houses[0]
        
        dp = [0] * n
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
        
        return dp[-1]

    n = len(money)
    if n == 1:
        return money[0]
    elif n == 2:
        return max(money[0], money[1])
    
    # 두 경우로 나누어 계산
    return max(rob_linear(money[:-1]), rob_linear(money[1:]))