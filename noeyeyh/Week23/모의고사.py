def solution(answers):
    a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answer = [0, 0, 0]
    
    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:
            answer[0] += 1
        if b[i % len(b)] == answers[i]:
            answer[1] += 1    
        if c[i % len(c)] == answers[i]:
            answer[2] += 1 
             
    max_score = max(answer)
    result = []
    
    for idx, score in enumerate(answer):
        if score == max_score:
            result.append(idx + 1)
            
    return result