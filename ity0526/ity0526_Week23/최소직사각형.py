def solution(sizes):
    max_width = 0
    max_height = 0

    for s in sizes:
        if s[0] < s[1]:
            tmp = s[0]
            s[0] = s[1]
            s[1] = tmp

        if max_width < s[0]:
            max_width = s[0]
        if max_height < s[1]:
            max_height = s[1]

    answer = max_width * max_height
    return answer