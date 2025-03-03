public class Solution {
    public int solution(String name) {
        int answer = 0;
        int n = name.length();
        int move = n - 1; // 기본적으로 오른쪽으로 쭉 가는 경우

        for (int i = 0; i < n; i++) {
            // 현재 문자 변경 비용 계산 (A와의 거리)
            answer += Math.min(name.charAt(i) - 'A', 'Z' - name.charAt(i) + 1);

            // 다음 A가 연속되는 지점 찾기
            int next = i + 1;
            while (next < n && name.charAt(next) == 'A') {
                next++;
            }

            // 좌우 이동 최소값 갱신
            move = Math.min(move, i * 2 + (n - next)); // 오른쪽 갔다가 왼쪽
            move = Math.min(move, (n - next) * 2 + i); // 왼쪽 갔다가 오른쪽
        }

        return answer + move;
    }
}