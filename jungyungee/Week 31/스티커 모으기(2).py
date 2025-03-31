def solution(sticker):
    
    if len(sticker) == 1:
        return sticker[0]

    dp_1 = [sticker[0], max(sticker[0], sticker[1])]
    for i in range(2, len(sticker)-1):
        dp_1.append(max(dp_1[i-2] + sticker[i], dp_1[i-1]))
    
    dp_2 = [0, sticker[1]]
    for i in range(2, len(sticker)):
        dp_2.append(max(dp_2[i-2] + sticker[i], dp_2[i-1]))
        
    return max(dp_1[-1], dp_2[-1])