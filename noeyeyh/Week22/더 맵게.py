import heapq

def solution(scoville, K):
    count = 0
    
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new = first + second * 2
        count += 1
        
        heapq.heappush(scoville, new)
        
    return count
