def solution(n, stations, w):
    answer = 0
    end = 0 
    for i in stations:
        start = max(i-w, 1)
        if start != 1:
            if (start - end - 1) % (2 * w + 1) == 0:
                answer += (start - end - 1) // (2 * w + 1)
            else:
                answer += (start - end - 1) // (2 * w + 1) + 1
        end = min(i+w, n)
    
    # 기지국이 세워진 곳을 기준으로 전부 확인 후, 기지국 뒤에 빈 곳이 있다면
    if end < n:
        answer += ( (n - end) + 2 * w) // (2 * w + 1)
    
    return answer