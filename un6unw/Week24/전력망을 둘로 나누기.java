import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int minDifference = Integer.MAX_VALUE;

        // 각 전선을 하나씩 끊어보면서 두 개의 네트워크 크기 차이를 계산
        for (int i = 0; i < wires.length; i++) {
            // 그래프 생성 (인접 리스트)
            List<List<Integer>> graph = new ArrayList<>();
            for (int j = 0; j <= n; j++) {
                graph.add(new ArrayList<>());
            }

            // 간선 추가 (단, i번째 간선은 제외)
            for (int j = 0; j < wires.length; j++) {
                if (j == i) continue; // 현재 끊을 간선은 추가하지 않음
                int a = wires[j][0];
                int b = wires[j][1];
                graph.get(a).add(b);
                graph.get(b).add(a);
            }

            // BFS 또는 DFS를 이용해 한쪽 네트워크 크기를 구함
            boolean[] visited = new boolean[n + 1];
            int count = getNetworkSize(graph, visited, 1); // 임의의 노드(1)에서 시작

            // 다른 네트워크 크기는 n - count
            int difference = Math.abs((n - count) - count);
            minDifference = Math.min(minDifference, difference);
        }

        return minDifference;
    }

    private int getNetworkSize(List<List<Integer>> graph, boolean[] visited, int node) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(node);
        visited[node] = true;
        int count = 1;

        while (!queue.isEmpty()) {
            int current = queue.poll();
            for (int next : graph.get(current)) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.add(next);
                    count++;
                }
            }
        }
        return count;
    }
}