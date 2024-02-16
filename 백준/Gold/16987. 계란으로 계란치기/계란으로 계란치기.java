import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] dur, weight;
    static int eggNum;
    static int total;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        eggNum = Integer.parseInt(br.readLine());

        dur = new int[eggNum];
        weight = new int[eggNum];

        for(int i=0; i < eggNum; i++) {
            String[] line = br.readLine().split(" ");
            dur[i] = Integer.parseInt(line[0]);
            weight[i] = Integer.parseInt(line[1]);
        }

        dfs(0);
        System.out.println(total);
    }

    public static void dfs(int next) {
        if (next >= eggNum) {
            int count = 0;
            for (int i=0; i < eggNum; i++) {
                if(dur[i] <= 0) {
                    count++;
                }
            }
            if (count >= total) total=count;
            return;
        }

        if (dur[next] <= 0) {
            dfs(next+1);
            return;
        }

        for (int i=0; i < eggNum; i++) {
            if (dur[i] >= 0 && i != next) {
                int opWeight = weight[i];
                int myWeight = weight[next];
                dur[i] -= myWeight;
                dur[next] -= opWeight;
                dfs(next+1);
                dur[i] += myWeight;
                dur[next] += opWeight;
            }
        }

        dfs(eggNum);
    }
}
