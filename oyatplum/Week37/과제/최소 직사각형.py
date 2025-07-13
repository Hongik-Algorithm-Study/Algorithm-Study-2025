def solution(sizes):
    w = []
    h = []
    for s in sizes:
        if s[0] > s[1]:
            w.append(s[0])
            h.append(s[1])
        else:
            w.append(s[1])
            h.append(s[0])

    return max(w) * max(h)