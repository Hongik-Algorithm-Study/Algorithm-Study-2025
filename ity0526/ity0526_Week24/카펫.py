def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            height = i
            width = yellow / i

            if brown == 2 * width + 2 * height + 4:
                return [width + 2, height + 2]