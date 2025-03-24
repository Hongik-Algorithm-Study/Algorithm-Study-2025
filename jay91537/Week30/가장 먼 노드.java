import java.util.*;
class Solution {
    public int solution(int n, int[][] edge) {
        List<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for(int[] e : edge) {
            int num1 = e[0];
            int num2 = e[1];
            graph.get(num1).add(num2);
            graph.get(num2).add(num1);
        }

        int[] answer = new int[n + 1];
        Arrays.fill(answer, n + 1);

        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        answer[1] = 0;

        while(!queue.isEmpty()) {
            int node = queue.poll();
            for(int next : graph.get(node)) {
                if(answer[next] > answer[node] + 1) {
                    answer[next] = answer[node] + 1;
                    queue.offer(next);
                }
            }
        }

        Arrays.sort(answer);
        int max = answer[answer.length-2];

        int count = 0;
        for(int i = answer.length-2; i >= 0; i--) {
            if(answer[i] != max) {
                break;
            }
            count++;
        }
        return count;
    }
}