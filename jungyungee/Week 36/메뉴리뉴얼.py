from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for i in course:
        comb_list = []

        for order in orders:
            sorted_order = sorted(order)
            comb_list += combinations(sorted_order, i)
        
        comb_counter = Counter(comb_list)
        
        if not comb_counter:
            continue

        max_count = max(comb_counter.values())
        
        if max_count >= 2:
            for menu, count in comb_counter.items():
                if count == max_count:
                    answer.append(''.join(menu))
    
    return sorted(answer)
