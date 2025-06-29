def solution(numbers, target):
    answer = 0

    def dfs(idx, sumNum, lastIdx):
        nonlocal answer
        if idx == lastIdx: #마지막까지 돈 경우
            if sumNum + numbers[idx] == target:
                answer += 1
            elif sumNum - numbers[idx] == target:
                answer += 1
        else:
            dfs(idx + 1, sumNum + numbers[idx], lastIdx)
            dfs(idx + 1, sumNum - numbers[idx], lastIdx)

    dfs(0, 0, len(numbers) - 1)

    return answer