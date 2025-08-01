def solution(nums):
    div = len(nums) // 2
    setNum = len(set(nums))

    if div < setNum:
        return div
    else:
        return setNum