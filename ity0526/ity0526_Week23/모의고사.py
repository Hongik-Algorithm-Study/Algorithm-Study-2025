def solution(answers):

    one = [1,2,3,4,5,1,2,3,4,5]
    two = [2,1,2,2,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    people = [one, two, three]
    correct = [0,0,0]

    for i, answer in enumerate(answers):
        problem = i%10

        for j in range(3):
            if people[j][problem] == answer:
                correct[j] += 1


    max_cor = max(correct)
    max_people = [i+1 for i, num in enumerate(correct) if num == max_cor]

    return max_people