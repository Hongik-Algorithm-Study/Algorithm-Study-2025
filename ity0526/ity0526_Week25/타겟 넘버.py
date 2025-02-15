def solution(numbers, target):

    total = sum(numbers)
    count = DFS(numbers, 0, total-target)

    return count


def DFS(numbers, sum_number1, differ):
    count = 0

    if sum_number1 > differ:
        return count

    for i in range(len(numbers)):
        sum_number2 = sum_number1 + numbers[i]*2

        pop_numbers = numbers[i+1:]

        if sum_number2 < differ:
            count += DFS(pop_numbers, sum_number2, differ)
        elif sum_number2 == differ:
            count += 1

    return count