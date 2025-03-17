import java.util.*;

class Solution {
    public int solution(int N, int number) {
        if (N == number) return 1;

        // dp[i]에는 N을 i번 사용해서 만들 수 있는 모든 수들을 저장합니다.
        List<Set<Integer>> dp = new ArrayList<>();
        for (int i = 0; i <= 8; i++) {
            dp.add(new HashSet<>());
        }

        // 1부터 8까지 N을 사용하는 경우의 수를 구합니다.
        for (int i = 1; i <= 8; i++) {
            int num = 0;
            // 예를 들어, N=5일 때 i가 3이면 555를 만듭니다.
            for (int j = 0; j < i; j++) {
                num = num * 10 + N;
            }
            dp.get(i).add(num);

            // 가능한 모든 분할 방식에 대해 사칙연산을 수행합니다.
            for (int j = 1; j < i; j++) {
                for (int a : dp.get(j)) {
                    for (int b : dp.get(i - j)) {
                        dp.get(i).add(a + b);
                        dp.get(i).add(a - b);
                        dp.get(i).add(b - a);
                        dp.get(i).add(a * b);
                        if (b != 0) dp.get(i).add(a / b);
                        if (a != 0) dp.get(i).add(b / a);
                    }
                }
            }

            // 현재 연산 결과에 number가 포함되어 있으면 i를 반환합니다.
            if (dp.get(i).contains(number)) {
                return i;
            }
        }

        // 8번 이하로 만들 수 없다면 -1을 반환합니다.
        return -1;
    }
}