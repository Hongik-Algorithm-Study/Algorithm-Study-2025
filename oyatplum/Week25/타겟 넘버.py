answer = 0
def dfs(numbers, target, cur, index):
    global answer
    if len(numbers) == index:
        if cur == target:
            answer += 1
        return
    dfs(numbers, target, cur + numbers[index], index + 1)
    dfs(numbers, target, cur - numbers[index], index + 1)

def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer