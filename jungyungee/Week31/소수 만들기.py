def solution(nums):
    even = list()
    odd = list()
    
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    
    sum_list = set([])
    sum = 0
    if (len(odd) >= 3):
        for i in range(len(odd)):
   