import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        Arrays.sort(d);  // 작은 금액부터 지원
        int count = 0;

        for (int cost : d) {
            if (budget >= cost) {
                budget -= cost;
                count++;
            } else {
                break;
            }
        }

        return count;
    }
}