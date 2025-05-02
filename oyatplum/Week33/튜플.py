def solution(s):
    answer = []
    temp = []
    temp.extend(s[2:len(s)-2].split("},{"))
    temp.sort(key=len) #요소 길이순 정렬

    visited = set() #방문 검사

    for i in temp:
        s = i.split(",")
        for j in s:
            if j not in visited:
                visited.add(j)
                answer.append(int(j))

    return answer