def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    for current in skill_trees:
        skill_list = list(skill)
        for i in list(current):
            if i not in skill_list:
                continue
            elif i == skill_list[0]:
                skill_list.pop(0)
            else:
                break          
        else:  # for 루프가 break 없이 정상 종료된 경우
            answer += 1
    return answer