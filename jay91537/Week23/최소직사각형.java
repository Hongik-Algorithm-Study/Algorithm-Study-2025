import java.util.*;

class Solution {
    public int solution(int[][] sizes) {

        int leftMax = 0;
        int rightMax = 0;
        for(int i=0;i<sizes.length;i++){
            if(sizes[i][0]<sizes[i][1]){
                int temp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = temp;
            }
            if(leftMax<sizes[i][0]) leftMax = sizes[i][0];
            if(rightMax<sizes[i][1]) rightMax = sizes[i][1];
        }

        return rightMax*leftMax;
    }
}