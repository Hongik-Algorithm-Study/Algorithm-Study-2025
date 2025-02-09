import java.util.*;

class Solution {
    static int maxNum = 0;
    public int solution(int k, int[][] dungeons) {

        permutation(dungeons, 0 ,dungeons.length-1, k);


        return maxNum;
    }

    public static void permutation(int[][] arr, int start, int end, int k) {

        if(start == end) {
            int checkNum = check(arr, k);
            if(checkNum > maxNum) {
                maxNum = checkNum;
            }

        } else {
            for(int i=start; i<=end; i++) {
                swap(arr, start, i);
                permutation(arr, start+1, end, k);
                swap(arr, start, i);
            }
        }

    }

    public static int check(int[][] dungeons, int k) {
        int answer = 0;
        for(int i=0; i<dungeons.length; i++) {
            if( k >= dungeons[i][0]) {
                k = k-dungeons[i][1];
                answer++;
            }
            else {
                break;
            }
        }

        return answer;
    }

    public static void swap(int[][] arr, int a, int b) {
        int tempA = arr[a][0];
        int tempB = arr[a][1];
        arr[a][0] = arr[b][0];
        arr[a][1] = arr[b][1];
        arr[b][0] = tempA;
        arr[b][1] = tempB;
    }
}