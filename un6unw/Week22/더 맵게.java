import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        // 최소 힙 생성
        PriorityQueue<Integer> heap = new PriorityQueue<>();

        // 모든 스코빌 지수를 힙에 추가
        for (int s : scoville) {
            heap.offer(s);
        }

        int mixCount = 0;

        // 가장 작은 값이 K 이상이 될 때까지 반복
        while (heap.size() > 1 && heap.peek() < K) {
            int first = heap.poll();    // 가장 작은 값
            int second = heap.poll();   // 두 번째로 작은 값

            // 새로운 음식의 스코빌 지수 계산
            int newScoville = first + (second * 2);
            heap.offer(newScoville);    // 힙에 추가

            mixCount++; // 섞은 횟수 증가
        }

        // 모든 음식이 K 이상이 되지 않으면 -1 반환
        return heap.peek() >= K ? mixCount : -1;
    }
}