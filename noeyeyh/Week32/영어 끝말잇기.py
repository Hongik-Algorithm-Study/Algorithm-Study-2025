def solution(n, words):
    answer = []
    
    for idx in range(len(words)):
        current = words[idx]
        
        # 이미 말했던 단어면 탈락
        if current in answer:
            return [(idx % n) + 1, (idx // n) + 1]
        
        # 끝말잇기 틀렸으면 탈락
        if idx > 0 and words[idx-1][-1] != current[0]:
            return [(idx % n) + 1, (idx // n) + 1]
        
        answer.append(current)
    
    # 탈락자 없을 경우
    return [0, 0]
