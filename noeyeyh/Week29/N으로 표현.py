def solution(N, number):
    if N == number:
        return 1

    # 최대 8번 사용할 수 있으므로, 1부터 8까지의 숫자를 저장할 리스트
    dp = [set() for _ in range(9)]
    
    # N을 이어 붙여서 만든 숫자 추가
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    
    # 사칙 연산을 통해 가능한 숫자 생성
    for i in range(1, 9):
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)

        if number in dp[i]:
            return i

    return -1
