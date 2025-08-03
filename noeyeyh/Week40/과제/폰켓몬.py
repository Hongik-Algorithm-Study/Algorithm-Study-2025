def solution(nums):
    count = len(set(nums))
    half = len(nums) // 2

    if count < half:
        answer = count
    else:
        answer = half

    return answer