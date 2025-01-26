import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public String solution(int[] numbers) {

        String[] arr = new String[numbers.length];

        for (int i = 0; i < numbers.length; i++)
            arr[i] = numbers[i] + "";

        Arrays.sort(arr, (n1, n2) -> (n2 + n1).compareTo(n1 + n2));

        return arr[0].equals("0") ? "0" : Arrays.stream(arr).collect(Collectors.joining());
    }
}