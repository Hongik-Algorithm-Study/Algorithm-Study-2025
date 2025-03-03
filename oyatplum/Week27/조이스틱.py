def solution(name):
    answer = 0
    #좌우 횟수
    cursorMove = len(name) - 1

    for i, spell in enumerate(name):
        #상하 횟수
        answer += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        #해당 문자 다음부터 연속된 A 찾기
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1
        #기존, 연속 A의 왼쪽부터, 오른쪽부터 중 최소
        cursorMove = min([cursorMove, 2*i + len(name) - next, i + 2*(len(name) - next)])

    return answer + cursorMove