from collections import deque

def solution(n, results):
    # 그래프 초기화
    wins = [[] for _ in range(n + 1)]  # 이긴 선수
    losses = [[] for _ in range(n + 1)]  # 진 선수

    # 경기 결과를 바탕으로 그래프 설정
    for winner, loser in results:
        wins[winner].append(loser)
        losses[loser].append(winner)

    def count_wins_and_losses(start):
        # BFS로 시작 선수로부터 도달할 수 있는 선수 수를 계산
        visited_wins = [False] * (n + 1)
        visited_losses = [False] * (n + 1)
        queue_wins = deque([start])
        queue_losses = deque([start])
        
        visited_wins[start] = True
        visited_losses[start] = True
        
        win_count = 0
        loss_count = 0
        
        # 이긴 선수 탐색
        while queue_wins:
            node = queue_wins.popleft()
            for neighbor in wins[node]:
                if not visited_wins[neighbor]:
                    visited_wins[neighbor] = True
                    win_count += 1
                    queue_wins.append(neighbor)

        # 진 선수 탐색
        while queue_losses:
            node = queue_losses.popleft()
            for neighbor in losses[node]:
                if not visited_losses[neighbor]:
                    visited_losses[neighbor] = True
                    loss_count += 1
                    queue_losses.append(neighbor)

        return win_count, loss_count

    total_rankable = 0

    # 각 선수에 대해 도달할 수 있는 선수 수 계산
    for i in range(1, n + 1):
        win_count, loss_count = count_wins_and_losses(i)
        # 이긴 선수 수와 진 선수 수의 합이 n-1과 같으면 순위를 알 수 있음
        if win_count + loss_count == n - 1:
            total_rankable += 1

    return total_rankable
