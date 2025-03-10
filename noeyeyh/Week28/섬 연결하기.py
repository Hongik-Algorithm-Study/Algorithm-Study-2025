def solution(n, costs):
    parent = {i: i for i in range(n)}

    # 루트 부모 찾기
    def find(v):
        if v != parent[v]:
            parent[v] = find(parent[v])
        return parent[v]

    answer = 0
    costs.sort(key=lambda x: x[2])  # 간선을 비용 기준으로 오름차순 정렬
    count = 0

    for v1, v2, w in costs:
        v1_set = find(v1)
        v2_set = find(v2)
        if v1_set != v2_set:
            parent[v1_set] = v2_set
            answer += w
            count += 1
            if count == n - 1:
                break

    return answer
