import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> bridge = new LinkedList<>();
        int totalWeight = 0;
        int time = 0;
        int idx = 0;

        // 1. 다리를 빈 자리로 채워 초기화
        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }

        // 2. 대기 트럭이 있을 동안 반복
        while (idx < truck_weights.length) {
            time++;
            // 맨 앞 트럭(혹은 빈 자리) 이동 완료
            totalWeight -= bridge.poll();

            // 다음 트럭 진입 가능 여부 판단
            if (totalWeight + truck_weights[idx] <= weight) {
                bridge.offer(truck_weights[idx]);
                totalWeight += truck_weights[idx];
                idx++;
            } else {
                // 못 들어가면 빈 칸으로 처리
                bridge.offer(0);
            }
        }

        // 마지막 트럭이 다 건널 시간을 포함
        return time + bridge_length;
    }
}