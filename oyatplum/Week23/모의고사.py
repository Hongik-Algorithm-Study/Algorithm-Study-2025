def solution(answers):
    answer = []
    person = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    temp = []

    count = 0
    for one in person:
        for i,j in zip(one, answers):
            if i == j:
                count += 1
        temp.append(count)
        count = 0

    maxP = max(temp)

    for i,j in enumerate(temp):
        if maxP == j:
            answer.append(i+1)

    return answer