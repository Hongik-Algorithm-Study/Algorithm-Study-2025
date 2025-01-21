from collections import deque

def solution(priorities, location):
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    answer = 0

    while queue:
        current = queue.popleft()
        
        # 현재 요소가 큐에서 가장 높은 우선순위인지 확인
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer

    return answer
