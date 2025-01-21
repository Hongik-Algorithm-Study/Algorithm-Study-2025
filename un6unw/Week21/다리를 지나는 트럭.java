import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> bridge = new LinkedList<>();
        int totalWeightOnBridge = 0; // 현재 다리 위의 총 무게
        int time = 0; // 경과 시간

        for (int truck : truck_weights) {
            while (true) {
                if (bridge.isEmpty()) {
                    // 다리가 비어 있으면 트럭을 올림
                    bridge.add(truck);
                    totalWeightOnBridge += truck;
                    time++; // 트럭이 올라가는 시간 추가
                    break;
                } else if (bridge.size() == bridge_length) {
                    // 다리가 꽉 차면 가장 앞의 트럭을 내림
                    totalWeightOnBridge -= bridge.poll();
                } else {
                    // 다리 위에 자리가 있을 때
                    if (totalWeightOnBridge + truck > weight) {
                        // 트럭을 올릴 수 없으면 빈 공간을 추가 (0을 넣음)
                        bridge.add(0);
                        time++;
                    } else {
                        // 트럭을 올릴 수 있으면 올림
                        bridge.add(truck);
                        totalWeightOnBridge += truck;
                        time++;
                        break;
                    }
                }
            }
        }

        // 마지막 트럭이 다리를 모두 건너는 시간 추가
        return time + bridge_length;
    }
}