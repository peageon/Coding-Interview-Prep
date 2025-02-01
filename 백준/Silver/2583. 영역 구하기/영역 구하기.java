import java.io.*;
import java.util.*;

public class Main {
    static int M, N, K;
    static int[][] board;
    static List<Integer> result;
    static int count;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        result = new ArrayList<>();
        count = 0;

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        board = new int[M][N];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int[] recs = new int[4];
            for (int j = 0; j < 4; j++) {
                recs[j] = Integer.parseInt(st.nextToken());
            }
            fillRec(recs);
        }

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 0) {
                    int numBox = dfs(j, i);
                    count++;
                    result.add(numBox);
                }
            }
        }
        Collections.sort(result);

        sb.append(count).append("\n");
        result.forEach(number -> sb.append(number).append(" "));

        System.out.println(sb);
    }

    private static int dfs(int x, int y) {
        if (y < 0 || y >= M || x < 0 || x >= N) {
            return 0;
        }
        if (board[y][x] == 0) {
            board[y][x] = 1;
            return 1 + dfs(x+1, y) + dfs(x, y -1) + dfs(x, y+1) + dfs(x-1, y);
        }
        return 0;
    }

    private static void fillRec(int[] recs) {
        for(int i = recs[0]; i < recs[2]; i++) {
            for (int j = recs[1]; j < recs[3]; j++) {
                board[j][i] = 1;
            }
        }
    }




}
