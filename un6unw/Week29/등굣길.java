class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int MOD = 1000000007;
        // 1-indexed로 사용하기 위해 (n+1) x (m+1) 크기의 배열 생성
        int[][] dp = new int[n + 1][m + 1];
        // 장애물(물웅덩이)을 표시할 boolean 배열
        boolean[][] isPuddle = new boolean[n + 1][m + 1];

        // 물웅덩이 위치 표시 (문제에서는 좌표가 1부터 시작합니다)
        for (int[] puddle : puddles) {
            int x = puddle[0];
            int y = puddle[1];
            if (x >= 1 && x <= m && y >= 1 && y <= n) {
                isPuddle[y][x] = true;
            }
        }

        // 시작 위치 초기화 (출발점 (1,1))
        dp[1][1] = 1;

        // dp 테이블 채우기: (i, j)로 도달하는 방법의 수는 위와 왼쪽의 합
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // 물웅덩이라면 경로 없음
                if (isPuddle[i][j]) {
                    dp[i][j] = 0;
                    continue;
                }
                // 출발점은 이미 초기화했으므로 건너뜁니다.
                if (i == 1 && j == 1) continue;

                // 위쪽 셀과 왼쪽 셀의 경로 수 합산
                dp[i][j] = ((i - 1 >= 1 ? dp[i - 1][j] : 0) + (j - 1 >= 1 ? dp[i][j - 1] : 0)) % MOD;
            }
        }

        return dp[n][m];
    }
}