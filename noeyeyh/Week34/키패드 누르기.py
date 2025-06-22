def solution(numbers, hand):
    answer = ''
    
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    # 초기 위치
    left_pos = keypad['*']
    right_pos = keypad['#']
    
    left_nums = [1, 4, 7]
    right_nums = [3, 6, 9]
    
    for num in numbers:
        if num in left_nums:
            answer += 'L'
            left_pos = keypad[num]
        elif num in right_nums:
            answer += 'R'
            right_pos = keypad[num]
        else:
            # 중심 키패드일 경우 거리 계산
            target = keypad[num]
            
            left_dist = abs(left_pos[0] - target[0]) + abs(left_pos[1] - target[1])
            right_dist = abs(right_pos[0] - target[0]) + abs(right_pos[1] - target[1])
            
            if left_dist < right_dist:
                answer += 'L'
                left_pos = target
            elif right_dist < left_dist:
                answer += 'R'
                right_pos = target
            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = target
                else:
                    answer += 'R'
                    right_pos = target
                    
    return answer
