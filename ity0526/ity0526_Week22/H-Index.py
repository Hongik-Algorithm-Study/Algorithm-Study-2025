def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)

    for i in range(len(citations), -1, -1):
        Ucount = 0
        Dcount = 0
        for j in citations:
            if j >= i :
                Ucount += 1
            if j <= i :
                Dcount += 1
        if Ucount >= i and Dcount <= i :
            answer = i
            break

    return answer