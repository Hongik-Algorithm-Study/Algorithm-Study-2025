import heapq, sys
def solution(n, s, a, b, fares):
    INF = sys.maxsize #최대

    maps = [[] for _ in range(n+1)] #fares 배열을 인접 리스트로

    for v,u,c in fares:
        maps[v].append((u,c))
        maps[u].append((v,c))


    def dij(start): #다익스트라 구현
        distance = [INF] * (n+1)
        distance[start] = 0
        q = [(0, start)]

        while q:
            curDist, curNode = heapq.heappop(q)

            if distance[curNode] < curDist: #꺼낸 노드가 더 짧은 거라면 스킵
                continue

            for nextNode, nextDist in maps[curNode]:
                if distance[nextNode] > curDist + nextDist:
                    distance[nextNode] = curDist + nextDist
                    heapq.heappush(q, (curDist + nextDist, nextNode))
        return distance

    D = [0] + [dij(i) for i in range(1, n+1)] #노드 번호가 1번부터 n번이니까 [0] 추가

    path = INF
    for i in range(1, n+1):
        path = min(path, D[s][i] + D[i][a] + D[i][b])

    return path