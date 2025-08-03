def solution(clothes):
    category_count = {}
    answer = 1
    
    for item, category in clothes:
        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1
        
    for count in category_count.values():
        answer *= (count + 1)
        
    return answer - 1