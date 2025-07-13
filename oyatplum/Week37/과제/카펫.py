def solution(brown, yellow):
    answer = []
    total = brown + yellow

    for i in range(1, total+1):
        if total % i == 0:
            w = i
            h = total // i

            if (w-2) * (h-2) == yellow:
                if w >= h:
                    answer.append(w)
                    answer.append(h)
                else:
                    answer.append(h)
                    answer.append(w)
                break

    return answer