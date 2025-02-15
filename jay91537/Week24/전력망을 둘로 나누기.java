import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;


        for(int i = 0; i < wires.length; i++){
            Map<Integer, List<Integer>> map = new HashMap<>();
            int[] union = new int[n+1];

            for(int j = 1; j < n+1; j++){
                union[j] = 1;
                map.put(j, new ArrayList<Integer>());
            }

            for(int j = 0; j < wires.length; j++){
                if(i == j) continue;

                int node1 = wires[j][0];
                int node2 = wires[j][1];

                map.get(node1).add(node2);
                map.get(node2).add(node1);
            }

            recursive(n, map, n, union);

            int countA = 0;
            int countB = 0;
            for(int j = 1; j < union.length; j++){
                if(union[j] == 1) countA++;
                else countB++;
            }

            answer = Math.min(answer, Math.abs(countA - countB));
        }
        return answer;
    }

    public void recursive(int start, Map<Integer, List<Integer>> map, int parent, int[] union){
        if(union[start] == parent) return;

        union[start] = parent;

        for(int v : map.get(start)){
            recursive(v, map, parent, union);
        }


    }

}