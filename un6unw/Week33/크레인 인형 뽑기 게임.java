import java.util.*;

public class Solution {
    public int solution(int[][] board, int[] moves) {
        Stack<Integer> basket = new Stack<>();
        int removedCount = 0;

        for (int move : moves) {
            int column = move - 1; // 배열은 0부터 시작하므로 -1

            for (int row = 0; row < board.length; row++) {
                int doll = board[row][column];

                if (doll != 0) { // 인형이 있다면
                    board[row][column] = 0; // 인형 뽑기 (0으로 비우기)

                    // 바구니가 비어있지 않고, 바구니 맨 위 인형과 같다면 제거
                    if (!basket.isEmpty() && basket.peek() == doll) {
                        basket.pop();
                        removedCount += 2;
                    } else {
                        basket.push(doll); // 그렇지 않으면 바구니에 담기
                    }
                    break; // 한 번만 뽑고 그 다음 move로 넘어감
                }
            }
        }

        return removedCount;
    }
}