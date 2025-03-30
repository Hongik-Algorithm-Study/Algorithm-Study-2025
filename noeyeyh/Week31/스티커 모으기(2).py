def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]

    def get_max_sticker_sum(sticker, start, end):
        dp = [0] * (end - start + 1)
        dp[0] = sticker[start]
        if end - start > 0:
            dp[1] = max(sticker[start], sticker[start + 1])

        for i in range(2, end - start + 1):
            dp[i] = max(dp[i - 2] + sticker[start + i], dp[i - 1])

        return dp[-1]

    # 첫 번째 스티커 포함
    case1 = get_max_sticker_sum(sticker, 0, n - 2)
    # 두 번째 스티커 포함
    case2 = get_max_sticker_sum(sticker, 1, n - 1)

    return max(case1, case2)
