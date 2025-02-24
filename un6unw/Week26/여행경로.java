import java.util.*;

class Solution {
    boolean[] visited;
    List<String> routes;

    public String[] solution(String[][] tickets) {
        visited = new boolean[tickets.length];
        routes = new ArrayList<>();

        Arrays.sort(tickets, (a, b) -> a[1].compareTo(b[1])); // 도착지를 기준으로 정렬

        dfs("ICN", "ICN", tickets, 0);

        return routes.get(0).split(" ");
    }

    private void dfs(String current, String path, String[][] tickets, int count) {
        if (count == tickets.length) {
            routes.add(path);
            return;
        }

        for (int i = 0; i < tickets.length; i++) {
            if (!visited[i] && tickets[i][0].equals(current)) {
                visited[i] = true;
                dfs(tickets[i][1], path + " " + tickets[i][1], tickets, count + 1);
                visited[i] = false;
            }
        }
    }
}