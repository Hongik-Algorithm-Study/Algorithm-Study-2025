import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        // 각 수포자의 찍기 패턴
        int[] pattern1 = {1, 2, 3, 4, 5};
        int[] pattern2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] pattern3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        // 각 수포자의 점수를 저장할 배열
        int[] scores = new int[3];

        // 정답과 비교하여 점수 계산
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == pattern1[i % pattern1.length]) scores[0]++;
            if (answers[i] == pattern2[i % pattern2.length]) scores[1]++;
            if (answers[i] == pattern3[i % pattern3.length]) scores[2]++;
        }

        // 가장 높은 점수를 찾기
        int maxScore = Math.max(scores[0], Math.max(scores[1], scores[2]));

        // 최고 점수를 받은 수포자 찾기
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 0; i < scores.length; i++) {
            if (scores[i] == maxScore) {
                result.add(i + 1);
            }
        }

        // ArrayList를 배열로 변환
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }

        return answer;
    }
}