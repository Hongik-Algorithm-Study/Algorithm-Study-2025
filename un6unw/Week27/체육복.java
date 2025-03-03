import java.util.Arrays;

public class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] students = new int[n];
        Arrays.fill(students, 1);

        for (int l : lost) {
            students[l - 1]--;
        }
        for (int r : reserve) {
            students[r - 1]++;
        }

        for (int i = 0; i < n; i++) {
            if (students[i] == 0) {
                if (i > 0 && students[i - 1] == 2) {
                    students[i]++;
                    students[i - 1]--;
                } else if (i < n - 1 && students[i + 1] == 2) {
                    students[i]++;
                    students[i + 1]--;
                }
            }
        }

        int count = 0;
        for (int s : students) {
            if (s > 0) count++;
        }

        return count;
    }
}