import java.util.*;

class Solution {
    static LinkedList<Integer> bridge = new LinkedList<>();
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0, totalWeight = 0;

        for (int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }

        for (int t : truck_weights) {
            while ((totalWeight + t - bridge.peek()) > weight) {
                totalWeight -= bridge.poll();
                bridge.add(0);
                answer += 1;
            }
            totalWeight -= bridge.poll();
            totalWeight += t;
            bridge.add(t);
            answer += 1;
        }

        return answer + bridge_length;
    }
}