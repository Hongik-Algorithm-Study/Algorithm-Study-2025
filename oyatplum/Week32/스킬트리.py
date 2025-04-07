def solution(skill, skill_trees):
    answer = 0
    skillList = list(skill)
    lenSkill = len(skillList) - 1

    for item in skill_trees:
        current = skillList[0] #배워야 할 스킬 첫번째로 초기화
        targetList = list(item)
        isTrue = 1
        temp = 0
        for target in targetList:
            if target not in skillList: #순서 상관없는 스킬인 경우
                continue
            else: #순서 지켜야 하는 경우
                if target == current: #순서 지킨 경우
                    if temp < lenSkill:
                        temp += 1
                        current = skillList[temp]
                    elif temp == lenSkill:
                        continue
                else: #순서 어긋난 경우
                    isTrue = 0
                    break

        if isTrue == 1:
            answer += 1

    return answer