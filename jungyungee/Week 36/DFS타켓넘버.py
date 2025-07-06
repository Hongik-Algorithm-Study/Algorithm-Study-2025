def solution(numbers, target):
    count = 0

    def dfs(idx, current_sum):
        nonlocal count
        
        if idx == len(numbers):  # 모든 숫자 다 썼을 때
            if current_sum == target:
                count += 1
            return
        # 다음 숫자를 + 또는 -로 더하기
        dfs(idx + 1, current_sum + numbers[idx])
        dfs(idx + 1, current_sum - numbers[idx])

    dfs(0, 0)  # 처음엔 인덱스 0, 합도 0부터 시작
    return count
