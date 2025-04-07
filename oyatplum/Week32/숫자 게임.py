def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a = 0
    b = 0

    while a < len(A) and b < len(B):
        if A[a] >= B[b]:
            b += 1
            continue
        else:
            answer += 1
            a += 1
            b += 1

    return answer