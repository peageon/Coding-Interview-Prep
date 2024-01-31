import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] tabs = new int[n+1];
        tabs[0] = 1;
        tabs[1] = 1;
        for(int i = 2; i <= n; i++ ) {
            tabs[i] = (tabs[i-1] + 2 * tabs[i-2]) % 10007;
        }

        System.out.println(tabs[n]);

    }
}
