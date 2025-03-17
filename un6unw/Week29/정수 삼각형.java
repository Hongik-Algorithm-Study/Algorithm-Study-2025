class Solution {
    public int solution(int[][] triangle) {
        int n = triangle.length;
        // 삼각형의 i번째 줄의 j번째 위치까지 도달했을 때의 최대 합
        int[][] dp = new int[n][n];


        dp[0][0] = triangle[0][0];

        // 삼각형의 각 줄에 대해 최대 경로 합 계산
        for (int i = 1; i < n; i++) {
            // 가장 왼쪽은 위에서 바로 내려오는 경우밖에 없음
            dp[i][0] = dp[i - 1][0] + triangle[i][0];

            // 가장 오른쪽은 왼쪽 위 대각선에서 내려오는 경우밖에 없음
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i];

            // 중간 원소들은 두 경로 중 큰 값 선택
            for (int j = 1; j < i; j++) {
                dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j];
            }
        }

        // 마지막 줄에서 최대 합을 찾습니다.
        int answer = 0;
        for (int i = 0; i < n; i++) {
            answer = Math.max(answer, dp[n - 1][i]);
        }

        return answer;
    }
}