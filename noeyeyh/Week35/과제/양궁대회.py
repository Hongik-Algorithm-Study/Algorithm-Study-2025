import copy
import math

def solution(n, info):
    max_diff = 0
    answer = [-1]

    def dfs(idx, arrows, lion_info):
        nonlocal max_diff, answer

        if arrows == n or idx == 11:
            # 화살이 남았으면 마지막에 몰아주기
            if arrows < n:
                lion_info[10] += n - arrows

            lion_score, appeach_score = 0, 0
            for i in range(11):
                if lion_info[i] > info[i]:
                    lion_score += 10 - i
                elif info[i] > 0:
                    appeach_score += 10 - i

            if lion_score > appeach_score:
                diff = lion_score - appeach_score
                if diff > max_diff:
                    max_diff = diff
                    answer = lion_info[:]
                elif diff == max_diff:
                    if lion_info[::-1] > answer[::-1]:
                        answer = lion_info[:]

            # 복구
            if arrows < n:
                lion_info[10] -= n - arrows
            return

        # 쏘고 이기기
        need = info[idx] + 1
        if arrows + need <= n:
            lion_info[idx] = need
            dfs(idx + 1, arrows + need, lion_info)
            lion_info[idx] = 0  # 복구

        # 안 쏘고 넘기기
        dfs(idx + 1, arrows, lion_info)

    dfs(0, 0, [0] * 11)
    return answer
