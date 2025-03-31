import java.util.Stack;

public class Solution {
    public String solution(String number, int k) {
        Stack<Character> stack = new Stack<>();
        int length = number.length();
        int targetLength = length - k; // 최종적으로 만들어야 할 숫자의 길이

        for (int i = 0; i < length; i++) {
            char digit = number.charAt(i);
            while (!stack.isEmpty() && k > 0 && stack.peek() < digit) {
                stack.pop();
                k--;
            }
            stack.push(digit);
        }

        // 결과를 저장할 char 배열
        char[] result = new char[targetLength];

        for (int i = 0; i < targetLength; i++) {
            result[i] = stack.get(i);
        }

        return new String(result);
    }
}