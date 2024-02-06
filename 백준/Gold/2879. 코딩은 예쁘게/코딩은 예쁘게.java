import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        String[] init = br.readLine().split(" ");
        String[] goal = br.readLine().split(" ");
        int[] diff = new int[N+1];

        for (int i=0; i < N ; i++) {
            diff[i+1] = Integer.parseInt(goal[i]) - Integer.parseInt(init[i]);
        }

        int total = 0;
        int prev = 0;

        for(int i=1; i < N+1; i++) {
            if(prev * diff[i] < 0) {
                total += Math.abs(prev);
            }
            else if(Math.abs(prev) >= Math.abs(diff[i])) {
                total += Math.abs(prev) - Math.abs(diff[i]);
            }
            prev = diff[i];
        }
        total += Math.abs(diff[N]);
        System.out.println(total);
    }
}