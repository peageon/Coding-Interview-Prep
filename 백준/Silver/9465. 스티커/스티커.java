import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(br.readLine());

        for (int i = 0; i < q; i++) {
            int n = Integer.parseInt(br.readLine());
            int[][] dk = new int[2][n];
            int[][] dp = new int[2][n];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int k=0; k < n; k++) {
                dk[0][k] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int k=0; k < n; k++) {
                dk[1][k] = Integer.parseInt(st.nextToken());
            }

            for (int k = 0; k < n; k++) {
                for (int j = 0; j < 2; j++) {
                    dp[j][k] = dk[j][k];
                    if(k >= 1) {
                        dp[j][k] = Math.max(dp[j][k], dk[j][k] + dp[(j+1)%2][k-1]);
                    }
                    if(k >= 2) {
                        dp[j][k] = Math.max(dp[j][k], dk[j][k]+dp[(j+1)%2][k-2]);
                    }
                }
            }

            int result = Math.max(dp[0][n-1], dp[1][n-1]);
            System.out.println(result);
        }
    }
}
