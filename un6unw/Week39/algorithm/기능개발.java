import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();

        for(int i = 0; i< progresses.length; i++){
            int remain = (100 - progresses[i]) / speeds[i];
            if((100 - progresses[i]) % speeds[i] != 0){
                remain += 1;
            }
            q.offer(remain);
        }

        while (!q.isEmpty()){
            int prevDay = q.poll();
            int count =1;

            while (!q.isEmpty() && q.peek() <= prevDay){
                q.poll();
                count++;
            }
            answer.add(count);
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}