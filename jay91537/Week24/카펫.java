import java.util.*;
import java.lang.Math;

class Solution {
    public int[] solution(int brown, int yellow) {

        int[] answer = {0,0};

        int sum = brown + yellow;
        int width =0;

        for(int i=1; i<=sum; i++) {
            if((sum%i==0) && i<=Math.sqrt(sum)) {
                width = sum/i;
                if(width * 2 + i * 2 - 4 == brown) {
                    answer[0] = width;
                    answer[1] = i;
                    break;
                }
            }
        }

        return answer;
    }
}