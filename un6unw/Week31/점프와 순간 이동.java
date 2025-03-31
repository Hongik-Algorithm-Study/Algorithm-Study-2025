class Solution {
    public int solution(int n) {
        int jumps = 0;
        while(n > 0) {
            // n이 홀수면 1을 빼야 점프를 해야 함
            if(n % 2 == 1) jumps++;
            // 짝수이거나 1을 뺀 후 n을 절반으로 줄임 (순간이동)
            n /= 2;
        }
        return jumps;
    }
}