def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:x[2])# 간선을 비용 기준으로 오름차순 정렬
    link = set([costs[0][0]])# 초기 연결된 노드(첫 번째 간선의 첫 번째 노드만 추가)

    while len(link) != n:# 모든 노드가 연결될 때까지 반복
        for v in costs:# 비용이 적은 간선부터 확인
            if v[0] in link and v[1] in link:# 이미 연결된 두 노드라면 건너뜀
                continue
            if v[0] in link or v[1] in link:# 둘 중 하나라도 연결된 경우
                link.update([v[0], v[1]])# 두 노드를 연결
                answer += v[2]# 비용 추가
                break# 하나의 간선만 추가하고 다시 while문 실행
    return answer