import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> queue = new LinkedList<>();

        // 큐 초기화
        for (int i = 0; i < priorities.length; i++) {
            queue.add(new int[]{i, priorities[i]}); // {문서의 인덱스, 우선순위}
        }

        int order = 0; // 출력 순서

        while (!queue.isEmpty()) {
            int[] current = queue.poll(); // 현재 문서
            boolean hasHigherPriority = false;

            // 나머지 문서 중 우선순위가 더 높은 문서가 있는지 확인
            for (int[] doc : queue) {
                if (doc[1] > current[1]) {
                    hasHigherPriority = true;
                    break;
                }
            }

            if (hasHigherPriority) {
                // 우선순위가 높은 문서가 있으면 현재 문서를 큐의 맨 뒤로 이동
                queue.add(current);
            } else {
                // 출력
                order++;
                if (current[0] == location) {
                    return order; // 내가 요청한 문서가 출력될 순서 반환
                }
            }
        }

        return -1; // 이론적으로 도달하지 않음
    }
}