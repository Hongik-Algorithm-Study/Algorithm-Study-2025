def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5] #5개
    second = [2, 1, 2, 3, 2, 4, 2, 5] #8개
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #10개
    temp = [0, 0, 0]

    for idx, i in enumerate(answers):
        if i == first[idx % 5]:
            temp[0] += 1
        if i == second[idx % 8]:
            temp[1] += 1
        if i == third[idx % 10]:
            temp[2] += 1

    maxNum = max(temp)

    for idx, t in enumerate(temp):
        if maxNum == t:
            answer.append(idx+1)
    return answer