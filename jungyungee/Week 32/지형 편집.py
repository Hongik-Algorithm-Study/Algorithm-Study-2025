##처음 코드

def solution(land, P, Q):
    answer = -1
    elements = sum(land,[])
    base = set(elements)
    sum_list = []

    for i in base:
        sum_element = 0
        for j in elements:
            if j > i:
                sum_element += (j-i) * Q
            elif i > j:
                sum_element += (i-j) * P
            else:
                continue
        sum_list.append(sum_element)
        
    answer = min(sum_list)
    
    return answer

##시간 초과 해결 코드

from bisect import bisect_left

def solution(land, P, Q):
    elements = sum(land,[])
    elements.sort()
    base = set(elements)
    n = len(elements)
    sum_list = []
    
     #누적합 (i 번째 까지의 합을 list에 저장)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + elements[i]
    
    # 각 기준마다 기준보다 작은 것, 큰 것에 따른 합 구해서 더하기
    for h in base:
        idx = bisect_left(elements, h) #h 보다 작은 것 개수
        
        # h보다 작은 애들
        low_count = idx  #h 보다 작은 것 개수
        low_sum = prefix_sum[idx] #h보다 작은 것들까지의 합
        cost_increase = (h * low_count - low_sum) * P # 추가해야하는 블럭 개수 * P

        # h보다 큰 애들
        high_count = n - idx  #h 보다 크거나 같은 것 개수
        high_sum = prefix_sum[n] - prefix_sum[idx] #h보다 큰 것들의 합(차이로 구함)
        cost_decrease = (high_sum - h * high_count) * Q # 제거해야하는 블럭 개수 * Q

        sum_element = cost_increase + cost_decrease
        sum_list.append(sum_element)
        
    print(sum_list)
    answer = min(sum_list)
    
    return answer