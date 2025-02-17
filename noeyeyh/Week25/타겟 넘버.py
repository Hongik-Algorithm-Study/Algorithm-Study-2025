def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for num in numbers:
        new_leaves = []
        
        for parent in leaves:
            new_leaves.append(parent + num)
            new_leaves.append(parent - num)
            
        leaves = new_leaves
        
    for leaf in leaves:
        if leaf == target:
            answer += 1
            
    return answer