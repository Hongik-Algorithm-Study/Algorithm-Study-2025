import java.util.Arrays;

public class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people); // 몸무게를 오름차순 정렬
        int lightest = 0; // 가장 가벼운 사람의 인덱스
        int boats = 0; // 필요한 보트 개수

        for (int heaviest = people.length - 1; heaviest >= lightest; heaviest--) {
            boats++; // 무거운 사람은 반드시 보트 사용

            // 가장 가벼운 사람과 함께 탈 수 있는지 확인
            if (people[lightest] + people[heaviest] <= limit) {
                lightest++; // 가벼운 사람도 태움
            }
        }

        return boats;
    }
}