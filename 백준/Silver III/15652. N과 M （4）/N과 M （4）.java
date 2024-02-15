import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N,M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inputs = br.readLine().split(" ");

        N = Integer.parseInt(inputs[0]);
        M = Integer.parseInt(inputs[1]);

        for (int i=1; i <= N; i++) {
            if(M > 1) {
                recurse(1, "", i);
            }
            else {
                System.out.println(i);
            }
        }

    }

    public static void recurse(int depth, String cur, int chosen) {
        if (depth == M) {
            System.out.println(cur + " " + chosen);
            return;
        }

        if(cur.isEmpty()) {
            cur = String.valueOf(chosen);
        }
        else {cur = cur + ' ' + chosen;}

        for (int i = chosen; i <= N; i++) {
            recurse(depth + 1, cur, i);
        }
    }
}