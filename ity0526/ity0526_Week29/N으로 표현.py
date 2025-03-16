def solution(N, number):
    dp = [set() for _ in range(9)]
    dp[1].add(N)

    if N == number:
        return 1

    for i in range(2, 9):

        concat_num = int(str(N) * i)
        if concat_num == number:
            return i
        else:
            dp[i].add(concat_num)

        for j in range(1, i):
            f, s = j, i - j

            for first in dp[f]:
                for second in dp[s]:
                    sum = first + second
                    minus = first - second
                    mul = first * second
                    div = mul
                    if second != 0:
                        div = first // second

                    if sum == number or minus == number or mul == number or div == number:
                        return i
                    else:
                        dp[i].update({sum, minus, mul, div})

    return -1