count = 0
def dfs(v, graph, visited, n):
    global count
    count += 1
    visited[v] = 1
    for i in range(n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i, graph, visited, n)
    return count

def solution(n, wires):
    graph = [[0]*(n+1) for _ in range(n+1)] #그래프 초기화
    visited = [] #방문한 노드
    temp = [] #절대값 저장 배열
    global count #노드 개수

    for i in wires: #전력망 끊기 전 모든 간선 추가
        graph[i[0]][i[1]] = 1
        graph[i[1]][i[0]] = 1

    for i in wires: #간선마다 돌아가며 제거
        graph[i[0]][i[1]] = 0 #여기가 제거하는 로직 0으로
        graph[i[1]][i[0]] = 0

        visited = [0] * (n+1) #방문한 노드 초기화
        a = dfs(i[0], graph, visited, n) #i[0]간선 첫번째 노드 기준으로 트리 돌기
        count = 0 #노드 개수 초기화

        visited = [0] * (n+1) #방문한 노드 초기화
        b = dfs(i[1], graph, visited, n) #i[1]간선 두번째 노드 기준으로 트리 돌기
        count = 0 #노드 개수 초기화

        temp.append(abs(a-b))

        graph[i[0]][i[1]] = 1 #제거한 간선 다시 추가!
        graph[i[1]][i[0]] = 1

    return min(temp)