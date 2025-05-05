import java.util.*;

public class Solution {
    Set<String> resultSet = new HashSet<>(); // 가능한 조합을 저장할 집합

    public int solution(String[] user_id, String[] banned_id) {
        boolean[] visited = new boolean[user_id.length];
        dfs(user_id, banned_id, 0, new ArrayList<>(), visited);
        return resultSet.size();
    }

    // 재귀 탐색 함수
    private void dfs(String[] user_id, String[] banned_id, int depth, List<String> current, boolean[] visited) {
        if (depth == banned_id.length) {
            // 현재 조합을 정렬해서 문자열로 만든 후 Set에 저장 (중복 제거)
            List<String> sorted = new ArrayList<>(current);
            Collections.sort(sorted);
            resultSet.add(String.join(",", sorted));
            return;
        }

        for (int i = 0; i < user_id.length; i++) {
            if (!visited[i] && isMatch(user_id[i], banned_id[depth])) {
                visited[i] = true;
                current.add(user_id[i]);

                dfs(user_id, banned_id, depth + 1, current, visited);

                visited[i] = false;
                current.remove(current.size() - 1); // 백트래킹
            }
        }
    }

    // user가 banned 패턴과 일치하는지 확인
    private boolean isMatch(String user, String banned) {
        if (user.length() != banned.length()) return false;

        for (int i = 0; i < user.length(); i++) {
            if (banned.charAt(i) == '*') continue;
            if (user.charAt(i) != banned.charAt(i)) return false;
        }

        return true;
    }
}