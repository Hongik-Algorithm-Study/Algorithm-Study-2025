import java.util.*;

class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();

        Map<Integer, int[]> pad = Map.of(
                1, new int[]{0,0}, 2, new int[]{0,1}, 3, new int[]{0,2},
                4, new int[]{1,0}, 5, new int[]{1,1}, 6, new int[]{1,2},
                7, new int[]{2,0}, 8, new int[]{2,1}, 9, new int[]{2,2},
                0, new int[]{3,1}
        );

        int[] left = {3, 0}, right = {3, 2};

        for(int i = 0; i < numbers.length; i++){
            int[] c = pad.get(numbers[i]);

            if(numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7){
                answer.append('L');
                left = c;
            }else if(numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9){
                answer.append('R');
                right = c;
            }else{
                int dl = Math.abs(left[0] - c[0]) + Math.abs(left[1] - c[1]);
                int dr = Math.abs(right[0] - c[0]) + Math.abs(right[1] - c[1]);

                if(dl < dr || (dl == dr && hand.equals("left"))){
                    answer.append('L');
                    left = c;
                }else{
                    answer.append('R');
                    right = c;
                }
            }
        }
        return answer.toString();
    }
}