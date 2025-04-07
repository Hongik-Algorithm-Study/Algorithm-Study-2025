import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        Arrays.sort(A); // A 오름차순 정렬
        Arrays.sort(B); // B 오름차순 정렬

        int aIndex = 0;
        int bIndex = 0;
        int score = 0;

        // B의 숫자가 A의 숫자보다 클 때만 점수 획득
        while (aIndex < A.length && bIndex < B.length) {
            if (B[bIndex] > A[aIndex]) {
                score++;
                aIndex++;
                bIndex++;
            } else {
                bIndex++;
            }
        }

        return score;
    }
}