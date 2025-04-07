def solution(nums):
    
    sum_list = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum_list.append(nums[i]+nums[j]+nums[k])
    
    result = 0
    for n in sum_list:
        check = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                check = False
                break
        if check == True:
            result += 1
    
    return result