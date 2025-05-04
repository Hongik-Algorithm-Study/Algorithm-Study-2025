public class Solution {
    public int solution(int[] stones, int k) {
        int left = 1;
        int right = 200_000_000; // stones 최대 값 범위
        int answer = 0;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (canCross(stones, k, mid)) {
                // mid 명까지는 건널 수 있음 → 더 많은 사람 시도
                answer = mid;
                left = mid + 1;
            } else {
                // mid 명은 못 건너므로 사람 수 줄임
                right = mid - 1;
            }
        }

        return answer;
    }

    // mid 명이 건널 수 있는지 확인하는 함수
    private boolean canCross(int[] stones, int k, int mid) {
        int count = 0; // 연속된 0의 개수

        for (int stone : stones) {
            if (stone < mid) {
                count++; // mid명보다 못 버티면 1 증가
                if (count >= k) {
                    return false; // k개 이상 연속 → 실패
                }
            } else {
                count = 0; // 연속 끊김
            }
        }

        return true; // 전부 순회해도 실패 조건 안 나오면 성공
    }
}