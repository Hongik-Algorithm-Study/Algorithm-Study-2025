class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int coverage = 2 * w + 1; // 한 기지국이 커버하는 집의 수
        int prev = 0; // 이전 기지국이 커버한 마지막 집 번호

        for (int station : stations) {
            int start = station - w; // 현재 기지국이 커버 시작하는 집 번호
            if (start > prev + 1) { // 이전 기지국과 현재 기지국 사이에 빈 구간이 있으면
                int gap = start - (prev + 1); // 빈 구간의 길이
                answer += (gap + coverage - 1) / coverage; // 필요한 기지국 수 계산
            }
            prev = station + w; // 현재 기지국이 커버하는 마지막 집 번호 갱신
        }

        // 마지막 기지국 이후의 빈 구간 처리
        if (prev < n) {
            int gap = n - prev;
            answer += (gap + coverage - 1) / coverage;
        }
        return answer;
    }
}