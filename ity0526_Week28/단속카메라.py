def solution(routes):
    routes.sort(key=lambda x: x[1])
    cameras = 0
    last = -30001

    for start, end in routes:
        if last < start:
            cameras += 1
            last = end

    return cameras