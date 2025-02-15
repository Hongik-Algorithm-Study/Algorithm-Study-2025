import java.util.*;

class Solution {
    private static final String VOWELS = "AEIOU";
    private List<String> dictionary = new ArrayList<>();

    public int solution(String word) {
        generateWords("", 0); // 모든 단어를 생성하여 리스트에 저장
        return dictionary.indexOf(word) + 1; // 단어의 위치 (1-based index)
    }

    private void generateWords(String current, int depth) {
        if (depth == 5) return; // 최대 길이 5 제한

        for (int i = 0; i < VOWELS.length(); i++) {
            String next = current + VOWELS.charAt(i);
            dictionary.add(next); // 사전에 추가
            generateWords(next, depth + 1); // 다음 문자 추가
        }
    }
}