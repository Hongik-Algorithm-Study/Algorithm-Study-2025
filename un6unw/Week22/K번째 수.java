import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for (int idx = 0; idx < commands.length; idx++) {
            int i = commands[idx][0];
            int j = commands[idx][1];
            int k = commands[idx][2];

            // 배열 자르기
            int[] slicedArray = Arrays.copyOfRange(array, i - 1, j);
            // 정렬
            Arrays.sort(slicedArray);
            // K번째 수 저장
            answer[idx] = slicedArray[k - 1];
        }

        return answer;
    }
}