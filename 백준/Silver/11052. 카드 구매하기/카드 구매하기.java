import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] deck = new int[n+1];
        for(int i = 1; i <= n; i++) {
            deck[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[n+1];
        dp[1] = deck[1];
        for(int i = 2; i <= n; i++ ) {
            int temp = deck[i];
            int mid = (i + 1) / 2;
            int cur = i - 1;
            while (cur >= mid) {
                int com = dp[cur] + dp[i - cur];
                if (com > temp) {
                    temp = com;
                }
                cur--;
            }
            dp[i] = temp;
        }
        System.out.println(dp[n]);
    }
}
