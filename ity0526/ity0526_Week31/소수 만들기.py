def solution(nums):
    answer = 0
    length = len(nums)
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                sum = nums[i] + nums[j] + nums[k]
                if is_prime(sum):
                    answer += 1

    return answer


def is_prime(num):
    if num % 2 == 0:
        return False

    for i in range(3, num, 2):
        if num % i == 0:
            return False

    return True