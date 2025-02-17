import java.util.*;

class Solution {

    public int solution(String begin, String target, String[] words) {

        int answer = 0;

        boolean[] visited = new boolean[words.length];

        answer = bfs(begin, target, words, visited, answer);

        return answer;
    }

    public int bfs(String begin, String target, String[] words, boolean visited[], int answer) {
        Queue<String> queue = new LinkedList<String>();

        queue.offer(begin);

        while(!queue.isEmpty()) {
            int size = queue.size();

            for(int i=0; i<size; i++) {
                String current = queue.poll();

                if (current.equals(target)) {
                    return answer;
                }

                for(int j=0; j<words.length; j++) {
                    if( !visited[j] && canTransfer(current, words[j]) ) {
                        queue.offer(words[j]);
                        visited[j]=true;
                    }
                }
            }
            answer++;
        }
        return 0;
    }

    public boolean canTransfer(String current, String canChanged) {
        int diffCount = 0; // 문자 차이를 나타낼 변수 초기화

        for (int i = 0; i < current.length(); i++) {
            if (current.charAt(i) != canChanged.charAt(i)) {
                diffCount++;
            }

            if (diffCount > 1) {
                return false;
            }
        }

        return diffCount == 1;
    }
}