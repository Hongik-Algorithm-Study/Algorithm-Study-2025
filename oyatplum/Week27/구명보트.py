from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while people:
        heaviest = people.pop()
        if people and people[0] + heaviest <= limit:
            people.popleft()
        answer += 1

    return answer