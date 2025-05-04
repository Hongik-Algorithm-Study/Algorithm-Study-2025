def solution(stones, k):
    start, end = 0, max(stones)
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        skipped = 0

        for stone in stones:
            if stone < mid:
                skipped += 1
                if skipped >= k:
                    break
            else:
                skipped = 0

        if skipped >= k:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer