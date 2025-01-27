def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, z = command
        new = array[i-1:j]
        new.sort()
        answer.append(new[z-1])
        
    return answer