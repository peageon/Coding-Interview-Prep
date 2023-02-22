import java.util.*;

public class Cbum {
    public static Integer bfs(List<Integer> current, List<List<Integer>>[] dp, Set<Character>[] dpt,
                              char[][] table, int row, int col) {
        int maximum = 1;
        Set<Character> stack = new HashSet<>();
        stack.add(table[current.get(0)][current.get(1)]);
        Deque<List> queue = new ArrayDeque<>();
        queue.add(new ArrayList(Arrays.asList(current, stack)));
        //System.out.print(queue);
        while(!queue.isEmpty()) {
            List vertex = queue.pollFirst();
            //System.out.println(vertex);
            List<Integer> cur_pos = (List<Integer>) vertex.get(0);
            //System.out.println(cur_pos.get(0));
            Set<Character> cur_stack = (Set<Character>) vertex.get(1);
            Set<Character> stackCopy = new HashSet<>(dpt[cur_pos.get(0) * col + cur_pos.get(1)]);
            stackCopy.removeAll(cur_stack);
            if (!stackCopy.isEmpty()) {
                //System.out.println(cur_stack.size());
                maximum = Math.max(cur_stack.size(), maximum);
            }
            List<List<Integer>> sidequests = new ArrayList<>(dp[cur_pos.get(0) * col + cur_pos.get(1)]);
            for(List<Integer> sidequest: sidequests) {
                //System.out.println(sidequest);
                if (!cur_stack.contains(table[sidequest.get(0)][sidequest.get(1)])) {
                    Set<Character> curStackCopy = new HashSet<>(cur_stack);
                    curStackCopy.add(table[sidequest.get(0)][sidequest.get(1)]);
                    queue.add(new ArrayList(Arrays.asList(sidequest, curStackCopy)));
                }
            }
        }
        return maximum+1;

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
        int[] X = {-1, 0, 1, 0};
        int[] Y = {0, -1, 0, 1};

        for(int test_case = 1; test_case <= T; test_case++) {
            int row = sc.nextInt();
            int col = sc.nextInt();
            sc.nextLine();
            List<List<Integer>>[] dp = new ArrayList[row*col];
            Set<Character>[] dpt = new Set[row*col];

            //Set Up Table
            char[][] table = new char[row][col];
            for(int i = 0; i < row; i++) {
                String tableRow = sc.nextLine();
                for(int j = 0; j < col; j++) {
                    table[i][j] = tableRow.charAt(j);
                }
            }
            int x, y;
            for(int r=0; r < row; r++) {
                for(int c=0; c < col; c++) {
                    for(int i=0; i < 4; i++) {
                        x = r + X[i];
                        y = c + Y[i];
                        if((0 <= x && x < row) && (0 <= y && y < col)){
                            List<Integer> temp = new ArrayList<Integer>(Arrays.asList(x, y));
                            if(dp[r*col + c] == null) {
                                dp[r*col + c] = new ArrayList<>();
                            }
                            dp[r * col + c].add(temp);
                            if(dpt[r * col + c] == null) {
                                dpt[r * col + c] = new HashSet<>();
                            }
                            dpt[r * col + c].add(table[x][y]);
                        }
                    }
                }
            }
            List<Integer> start = new ArrayList<>();
            start.add(0);
            start.add(0);
            System.out.printf("#%d %d%n", test_case, bfs(start, dp, dpt, table, row, col));
        }
    }
}
