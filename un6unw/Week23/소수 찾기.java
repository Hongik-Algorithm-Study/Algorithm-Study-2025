import java.util.HashSet;

class Solution {
    private HashSet<Integer> numberSet = new HashSet<>();

    public int solution(String numbers) {
        //가능한 모든 숫자 조합을 생성
        boolean[] visited = new boolean[numbers.length()];
        generatePermutations(numbers, "", visited);

        //소수 판별 및 개수 세기
        int count = 0;
        for (int num : numberSet) {
            if (isPrime(num)) {
                count++;
            }
        }

        return count;
    }

    // 순열을 생성하는 메서드 (백트래킹 사용)
    private void generatePermutations(String numbers, String current, boolean[] visited) {
        if (!current.isEmpty()) {
            numberSet.add(Integer.parseInt(current));
        }

        for (int i = 0; i < numbers.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                generatePermutations(numbers, current + numbers.charAt(i), visited);
                visited[i] = false;
            }
        }
    }

    // 소수 판별 메서드
    private boolean isPrime(int num) {
        if (num < 2) return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
