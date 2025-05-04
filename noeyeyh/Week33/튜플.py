def solution(s):
    s = s[2:-2]  # 앞뒤 {{ }} 제거
    parts = s.split("},{")  # 튜플 단위로 나누기
    tuples = [list(map(int, part.split(','))) for part in parts]
    
    # 튜플을 길이 기준으로 정렬
    tuples.sort(key=len)
    
    answer = []
    seen = set()
    for t in tuples:
        for num in t:
            if num not in seen:
                answer.append(num)
                seen.add(num)
    return answer