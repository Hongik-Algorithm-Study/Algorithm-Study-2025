def solution(n, computers):
    count = 0   
    visited = [False] * n   

    def dfs(current_node):
        visited[current_node] = True
        
        for adjacent_node in range(n):
            if not visited[adjacent_node] and computers[current_node][adjacent_node]:
                dfs(adjacent_node)

    for node_index in range(n):
        if not visited[node_index]:
            dfs(node_index)
            count += 1
    
    return count