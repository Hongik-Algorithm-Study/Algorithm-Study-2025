class Solution {
    public int solution(int[] money) {
        int answer = 0;
        int n = money.length;

        int dp[] = new int[n+1];

        for(int i = 0; i <= 1; i++){
            int end_index;

            if(i == 0){ // 1번집 안 털 경우
                dp[1] = 0;
                end_index = n;

            } else{ // 1번집 털 경우
                dp[1] = money[0];
                end_index = n-1;
            }

            for(int j = 2; j <= end_index; j++){
                dp[j] = Math.max(dp[j-2] + money[j-1], dp[j-1]);
            }

            answer = Math.max(answer, dp[end_index]);
        }
        return answer;
    }
}