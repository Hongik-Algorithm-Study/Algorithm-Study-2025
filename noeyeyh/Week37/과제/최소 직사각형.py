def solution(sizes):
    answer = 0
    max_w = 0
    max_h = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    max_w = max(size[0] for size in sizes)
    max_h = max(size[1] for size in sizes)
    
    answer = max_w * max_h
    return answer