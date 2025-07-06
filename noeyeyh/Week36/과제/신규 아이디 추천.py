import re

def solution(new_id):
    # 1단계: 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2단계: 허용되지 않은 문자 제거
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    
    # 3단계: 마침표 2번 이상을 하나로 치환
    new_id = re.sub(r'\.{2,}', '.', new_id)
    
    # 4단계: 처음과 끝의 마침표 제거
    new_id = new_id.strip('.')
    
    # 5단계: 빈 문자열이면 "a" 대입
    if not new_id:
        new_id = 'a'
    
    # 6단계: 16자 이상이면 앞 15자만, 끝에 . 제거
    new_id = new_id[:15].rstrip('.')
    
    # 7단계: 길이가 2자 이하라면 마지막 문자를 길이 3이 될 때까지 반복
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
