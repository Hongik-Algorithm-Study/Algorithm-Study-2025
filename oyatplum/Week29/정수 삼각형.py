def solution(triangle):
    saveList = [triangle[0][0]]

    for floor in triangle[1:]:
        temp = [0] * len(floor)
        for i, item in enumerate(floor):
            if i == 0:
                temp[i] = saveList[0] + item
            elif i == len(floor)-1:
                temp[i] = saveList[i-1] + item
            else:
                temp[i] = max(saveList[i-1] + item, saveList[i] + item)
        saveList = temp
    return max(saveList)