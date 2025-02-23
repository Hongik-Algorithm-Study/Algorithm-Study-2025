import java.util.*;

class Solution {
    public List<String> solution(String[][] tickets) {

        List<String> answer = new ArrayList<>();
        answer.add("ICN");
        boolean[] visited = new boolean[tickets.length];

        dfs("ICN", tickets, visited, answer);

        return answer;
    }

    public void dfs(String start, String[][] tickets, boolean[] visited, List<String> answer) {

        List<String> temp = new ArrayList<>();
        HashMap<String, Integer> indexTemp = new HashMap<>();

        for(int i=0; i<tickets.length; i++) {
            if(visited[i] == false && tickets[i][0].equals(start)) {

                temp.add(tickets[i][1]);
                indexTemp.put(tickets[i][1], i);
            }
        }
        System.out.println(temp);

        if(temp.isEmpty()) return;
        if(!temp.isEmpty()) Collections.sort(temp);

        if(!temp.isEmpty()) {
            for(int j=0; j<temp.size(); j++) {

                visited[indexTemp.get(temp.get(j))] = true;
                answer.add(temp.get(j));

                System.out.println(answer);
                for(int a=0; a<visited.length; a++) {
                    System.out.println(visited[a]);
                }

                dfs(tickets[indexTemp.get(temp.get(j))][1], tickets, visited, answer);
                for(int k=0; k<visited.length; k++) {
                    if(visited[k]==false) break;

                    if(k==visited.length-1) return;
                }
                System.out.println(temp.get(j));
                answer.remove(temp.get(j));
                visited[indexTemp.get(temp.get(j))] = false;
            }
        }
    }
}
