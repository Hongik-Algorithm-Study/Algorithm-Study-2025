def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = {i: i for i in range(n)}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    total = 0
    for u, v, cost in costs:
        if find(u) != find(v):
            union(u, v)
            total += cost

    return total