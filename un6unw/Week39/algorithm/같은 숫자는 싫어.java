import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        if(arr == null || arr.length == 0){
            return new int[0];
        }

        Stack<Integer> stack = new Stack<>();
        for(int num : arr) {
            if(stack.isEmpty() || stack.peek() != num){
                stack.push(num);
            }
        }
        int size = stack.size();
        int[] answer = new int[size];
        for (int i = size - 1; i >= 0; i--){
            answer[i] = stack.pop();
        }
        return answer;
    }
}