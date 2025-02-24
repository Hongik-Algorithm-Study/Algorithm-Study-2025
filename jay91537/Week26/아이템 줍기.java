import java.util.*;

class Solution {

    static char[][] map = new char[101][101];

    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        for(int i=0;i<rectangle.length;i++){
            int y1=rectangle[i][1];
            int x1=rectangle[i][0];
            int y2=rectangle[i][3];
            int x2=rectangle[i][2];
            draw(x1*2,y1*2,x2*2,y2*2);
        }

        return bfs(characterX*2, characterY*2,itemX*2,itemY*2);
    }

    public static int bfs(int X, int Y, int itemX, int itemY) {

        int[][] vector = {{1,0},{-1,0},{0,1},{0,-1}};

        Queue<Integer[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[101][101];

        queue.add(new Integer[]{X,Y,0}); // 마지막은 count 값
        while(!queue.isEmpty()) {
            Integer temp[]=queue.poll();

            if(temp[0]==itemX && temp[1]==itemY) return temp[2]/2;

            int x = temp[0];
            int y = temp[1];
            int count = temp[2];

            for(int i=0; i<4; i++) {
                int nextX = x + vector[i][0];
                int nextY = y + vector[i][1];
                if( nextX > 0 && nextX < map.length && nextY >0 && nextY < map.length
                        && map[nextX][nextY]=='2' && visited[nextX][nextY]==false) {
                    visited[nextX][nextY]=true;
                    queue.offer(new Integer[]{nextX, nextY, count+1});
                }
            }

        }
        return 0;

    }

    public static void draw(int x1, int y1, int x2, int y2) {
        for(int i=x1;i<=x2;i++){
            for(int j=y1;j<=y2;j++){
                if(map[i][j]=='1') continue;
                map[i][j]='1';
                if(i==x1||i==x2||j==y1||j==y2)
                    map[i][j]='2';
            }
        }
    }
}