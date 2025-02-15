import java.util.*;

class Solution {
    private int maxDungeons = 0;

    public int solution(int k, int[][] dungeons) {
        int n = dungeons.length;
        int[] order = new int[n];
        for (int i = 0; i < n; i++) {
            order[i] = i; // 던전 인덱스 저장
        }

        // 모든 순열 탐색
        permute(order, 0, k, dungeons);

        return maxDungeons;
    }

    private void permute(int[] order, int depth, int k, int[][] dungeons) {
        if (depth == order.length) {
            maxDungeons = Math.max(maxDungeons, countDungeons(k, order, dungeons));
            return;
        }

        for (int i = depth; i < order.length; i++) {
            swap(order, depth, i);
            permute(order, depth + 1, k, dungeons);
            swap(order, depth, i); // 원래 상태로 되돌리기
        }
    }

    private int countDungeons(int k, int[] order, int[][] dungeons) {
        int count = 0;
        for (int i : order) {
            if (k >= dungeons[i][0]) { // 최소 필요 피로도 충족
                k -= dungeons[i][1]; // 소모 피로도 차감
                count++;
            } else {
                break;
            }
        }
        return count;
    }

    private void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}