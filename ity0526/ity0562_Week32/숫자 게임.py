def solution(A, B):
    A.sort()
    B.sort()

    count = 0
    a_idx = 0
    b_idx = 0
    n = len(A)

    while a_idx < n and b_idx < n:
        if B[b_idx] > A[a_idx]:
            count += 1
            a_idx += 1
            b_idx += 1
        else:
            b_idx += 1

    return count