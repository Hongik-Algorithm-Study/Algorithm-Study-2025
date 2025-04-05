def solution(skill, skill_trees):
    count = 0
    
    for i in skill_trees:
        new = ""
        for j in i:
            if j in skill:
                new += j
                
        if skill.startswith(new):
            count += 1
            
    return count