def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(targetIdx):
        nonlocal visited

        for idx, computer in enumerate(computers[targetIdx]):
            if idx != targetIdx and visited[idx] != 1 and computer == 1: #조건에 만족하면
                visited[idx] = 1 #방문 처리
                dfs(idx)

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1 #방문 처리
            dfs(i)
            answer += 1 #네트워크 개수 추가
        else:
            continue #이미 네트워크 연결된 노드의 경우

    return answer