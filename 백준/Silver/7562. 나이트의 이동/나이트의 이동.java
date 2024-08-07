import java.io.*;
import java.util.*;

public class Main {
    static int L;
    static boolean visit[][];
    static boolean board[][];
    static int[] dx = {-2, -1, 1, 2, -2, -1, 1, 2};
    static int[] dy = {1, 2, 2, 1, -1, -2, -2, -1};
    static int count;
    static int sx, sy, ex, ey;

    static void bfs(int x, int y) {
        Queue<int[]> qu = new LinkedList<int[]>();
        qu.add(new int[] {x, y, 0});
        int c;

        while(!qu.isEmpty()) {
            x = qu.peek()[0];
            y = qu.peek()[1];
            c = qu.peek()[2];
            if (visit[x][y] == true) {
                qu.poll();
                continue;
            }
            visit[x][y] = true;

            if (x == ex && y == ey) {
                count = c;
                return;
            }
            for (int i = 0; i < 8; i++) {
                int cx = x + dx[i];
                int cy = y + dy[i];

                if (cx >= 0 && cy >= 0 && cx < L && cy < L) {
                    qu.add(new int[] {cx, cy, c+1});
                }
            }
            qu.poll();
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i=0; i < t; i++) {
            count = 0;
            L = Integer.parseInt(br.readLine());
            board = new boolean[L][L];
            visit = new boolean[L][L];
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            sx = Integer.parseInt(st.nextToken());
            sy = Integer.parseInt(st.nextToken());
            StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
            ex = Integer.parseInt(st2.nextToken());
            ey = Integer.parseInt(st2.nextToken());

            bfs(sx, sy);
            System.out.println(count);
        }
    }
}
