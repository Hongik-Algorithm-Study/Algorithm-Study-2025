def solution(n, lost, reserve):
    #여벌 도난 경우
    reserveSet = set(reserve) - set(lost)
    lostSet = set(lost) - set(reserve)

    for i in sorted(reserveSet):
        if i - 1 in lostSet:
            lostSet.remove(i - 1)
        elif i + 1 in lostSet:
            lostSet.remove(i + 1)

    return n - len(lostSet)