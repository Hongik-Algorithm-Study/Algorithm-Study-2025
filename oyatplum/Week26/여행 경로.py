count = 0
def dfs(tickets, start, visited, t, answer):
    for index, ticket in enumerate(tickets):
        if ticket[0] == start[1] and visited[index] == 0:
            copiedVisited = visited.copy()
            copiedT = t.copy()
            copiedT.append(ticket[1])
            copiedVisited[index] = 1
            dfs(tickets, ticket, copiedVisited, copiedT, answer)


    if len(t) == count+1:
        answer.append(t)

def solution(tickets):
    temp = []
    answer = []
    global count
    count = len(tickets)

    for index, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            temp.append([ticket,index])

    for i in temp:
        visited = [0]*(len(tickets))
        visited[i[1]] = 1
        t = ["ICN", i[0][1]]
        dfs(tickets, i[0], visited, t, answer)

    answer.sort()
    return answer[0]