import java.util.*;

class Solution {
    public int solution(int[][] maps) {

        Queue<int[]> queue = new LinkedList<int[]>();
        int[][] vector = { {0,1} , {1,0} , {0,-1} , {-1,0} };

        queue.offer(new int[]{0,0,1});

        while(!queue.isEmpty()) {
            int size = queue.size();


            for(int i=0; i<size; i++) {
                int[] current = queue.poll();

                if( current[0] == maps.length-1 && current[1] == maps[0].length-1
                ) {
                    return current[2];
                }

                for(int j=0; j<4; j++) {
                    if( current[0]+vector[j][0]>=0 && current[0]+vector[j][0] < maps.length && current[1]+vector[j][1] >= 0 && current[1]+vector[j][1] < maps[0].length && maps[current[0]+vector[j][0]][current[1]+vector[j][1]]==1 ) {
                        queue.offer(new int[]{current[0]+vector[j][0], current[1]+vector[j][1],current[2]+1 });
                        maps[current[0]+vector[j][0]][current[1]+vector[j][1]]=0;

                    }
                }
            }
        }


        return -1;
    }
}