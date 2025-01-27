import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        // 논문 인용 횟수 배열 정렬 (오름차순)
        Arrays.sort(citations);

        int n = citations.length;
        for (int i = 0; i < n; i++) {
            // 현재 논문이 H-Index 조건을 만족하는지 확인
            int h = n - i; // 남은 논문의 수
            if (citations[i] >= h) {
                return h;
            }
        }

        return 0; // 조건을 만족하는 H-Index가 없는 경우
    }
}