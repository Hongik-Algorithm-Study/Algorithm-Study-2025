def solution(numbers, hand):
    answer = ''
    curL = '*'
    curR = '#'
    dis = [[0,4,3,4,3,2,3,2,1,2],
           [4,0,1,2,1,2,3,2,3,4],
           [3,1,0,1,2,1,2,3,2,3],
           [4,2,1,0,3,2,1,4,3,2],
           [3,1,2,3,0,1,2,1,2,3],
           [2,2,1,2,1,0,1,2,1,2],
           [3,3,2,1,2,1,0,3,2,1],
           [2,2,3,4,1,2,3,0,1,2],
           [1,3,2,3,2,1,2,1,0,1],
           [2,4,3,2,3,2,1,2,1,0],
           [1,3,4,5,2,3,4,1,2,3], # *인 경우
           [1,5,4,3,4,3,2,3,2,1]  # #인 경우
           ]
    for target in numbers:
        if target == 1 or target == 4 or target == 7:
            curL = target
            answer += 'L'
        elif target == 3 or target == 6 or target == 9:
            curR = target
            answer += 'R'
        else: # 2, 5, 8, 0인 경우
            if curL == '*':
                disL = dis[10][target]
            else:
                disL = dis[curL][target]
            if curR == '#':
                disR = dis[11][target]
            else:
                disR = dis[curR][target]

            if disL > disR:
                curR = target
                answer += 'R'
            elif disL < disR:
                curL = target
                answer += 'L'
            else: #거리 같은 경우 어떤 손인지
                if hand == "left":
                    curL = target
                    answer += 'L'
                else:
                    curR = target
                    answer += 'R'

    return answer