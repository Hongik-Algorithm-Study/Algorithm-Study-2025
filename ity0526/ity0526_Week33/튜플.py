def solution(s):
    s = s[2:-2].split("},{")
    s = [set(map(int, x.split(','))) for x in s]
    s.sort(key=len)

    answer = []
    seen = set()

    for group in s:
        num = (group - seen).pop()
        answer.append(num)
        seen.add(num)

    return answer