import java.util.*;

public class Solution {
    public int[] solution(String s) {
        // 숫자 등장 횟수를 저장할 Map
        Map<Integer, Integer> countMap = new HashMap<>();

        // 문자열에서 숫자만 추출
        String numbersOnly = s.replaceAll("[^0-9]", " ");
        String[] nums = numbersOnly.trim().split("\\s+");

        // 각 숫자의 등장 횟수 세기
        for (String numStr : nums) {
            int num = Integer.parseInt(numStr);
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // 숫자와 등장 횟수를 리스트로 분리
        List<Integer> keys = new ArrayList<>();
        List<Integer> values = new ArrayList<>();
        for (int key : countMap.keySet()) {
            keys.add(key);
            values.add(countMap.get(key));
        }

        // 단순 선택 정렬 방식으로 등장 횟수 기준 내림차순 정렬
        for (int i = 0; i < values.size() - 1; i++) {
            for (int j = i + 1; j < values.size(); j++) {
                if (values.get(i) < values.get(j)) {
                    // 값 교환
                    int tempVal = values.get(i);
                    values.set(i, values.get(j));
                    values.set(j, tempVal);

                    // 키도 함께 교환
                    int tempKey = keys.get(i);
                    keys.set(i, keys.get(j));
                    keys.set(j, tempKey);
                }
            }
        }

        // 결과 배열 생성
        int[] answer = new int[keys.size()];
        for (int i = 0; i < keys.size(); i++) {
            answer[i] = keys.get(i);
        }

        return answer;
    }
}