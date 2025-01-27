import java.util.Arrays;

class Solution {
    public String solution(int[] numbers) {
        // 숫자 배열을 문자열 배열로 변환
        String[] numStrs = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            numStrs[i] = String.valueOf(numbers[i]);
        }

        // 문자열 배열 정렬: (x + y)와 (y + x)를 비교
        Arrays.sort(numStrs, (x, y) -> (y + x).compareTo(x + y));

        // 정렬된 문자열 배열을 하나로 합침
        StringBuilder answer = new StringBuilder();
        for (String num : numStrs) {
            answer.append(num);
        }

        // 결과가 "0"으로 시작하면 "0" 반환
        if (answer.charAt(0) == '0') {
            return "0";
        }

        return answer.toString();
    }
}