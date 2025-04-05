import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        Set<String> usedWords = new HashSet<>();
        usedWords.add(words[0]);

        for (int i = 1; i < words.length; i++) {
            String prev = words[i - 1];
            String curr = words[i];

            // 끝말잇기 규칙 위반 또는 중복 단어 사용 시
            if (usedWords.contains(curr) || prev.charAt(prev.length() - 1) != curr.charAt(0)) {
                int person = (i % n) + 1;       // 사람 번호 (1부터 시작)
                int round = (i / n) + 1;        // 몇 번째 차례인지
                return new int[]{person, round};
            }

            usedWords.add(curr);
        }

        return new int[]{0, 0}; // 모든 단어가 규칙을 잘 지킨 경우
    }
}