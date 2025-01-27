import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break

        mix(scoville)
        answer += 1

    return answer


def mix(scoville):
    first = heapq.heappop(scoville)
    second = heapq.heappop(scoville)
    mixed = first + second * 2
    heapq.heappush(scoville, mixed)