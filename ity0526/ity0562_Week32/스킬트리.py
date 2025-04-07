def solution(skill, skill_trees):
    answer = len(skill_trees)
    s_index = 0

    for skill_tree in skill_trees:
        for s in skill_tree:
            if s in skill:
                if s == skill[s_index]:
                    s_index += 1
                else:
                    answer -= 1
                    break

        s_index = 0

    return answer