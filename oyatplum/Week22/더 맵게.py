import heapq
def solution(scoville, K):
    shake = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        new = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville,new)
        shake += 1

    return shake