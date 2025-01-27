def solution(array, commands):
    answer = []

    for command in commands :
        sort_arr = sorted(array[command[0]-1 : command[1]-1])
        answer.append(sort_arr[command[2]-1])

    return answer