import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] dp, tri;
    static int left, right, result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        tri = new int[N][N];
        dp = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int ct = st.countTokens();
            for (int j = 0; j < ct; j++) {
                tri[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp[0][0] = tri[0][0];
        for (int i = 0; i < N - 1; i++) {
            for (int j = 0; j <= i; j++) {
                left = dp[i][j] + tri[i + 1][j];
                right = dp[i][j] + tri[i + 1][j + 1];
                dp[i + 1][j] = Math.max(dp[i + 1][j], left);
                dp[i + 1][j + 1] = Math.max(dp[i + 1][j + 1], right);
            }
        }

        result = Arrays.stream(dp[N-1]).max().getAsInt();
        System.out.println(result);


    }


}
