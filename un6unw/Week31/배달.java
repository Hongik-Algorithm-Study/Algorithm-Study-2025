import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        // 인접 리스트 생성 (1번부터 N번까지 사용)
        List<int[]>[] graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] r : road) {
            int a = r[0], b = r[1], c = r[2];
            // 양방향 도로이므로 양쪽 모두 추가
            graph[a].add(new int[]{b, c});
            graph[b].add(new int[]{a, c});
        }

        // 각 마을까지의 최소 시간을 저장할 배열
        int[] dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[1] = 0;

        // 우선순위 큐: int[] {마을번호, 현재까지 소요 시간}
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));
        pq.offer(new int[]{1, 0});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int curVillage = cur[0], curTime = cur[1];
            // 이미 더 빠른 경로가 있다면 건너뜁니다.
            if (curTime > dist[curVillage]) continue;

            for (int[] next : graph[curVillage]) {
                int nextVillage = next[0];
                int nextTime = curTime + next[1];
                if (nextTime < dist[nextVillage]) {
                    dist[nextVillage] = nextTime;
                    pq.offer(new int[]{nextVillage, nextTime});
                }
            }
        }

        // K 시간 이하로 도착 가능한 마을의 수 계산
        int count = 0;
        for (int i = 1; i <= N; i++) {
            if (dist[i] <= K) count++;
        }
        return count;
    }
}