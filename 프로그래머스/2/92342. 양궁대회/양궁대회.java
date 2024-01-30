import java.util.*;
class Solution {
    private static int[] cur = new int[11];
    private static int maxDiff = Integer.MIN_VALUE;
    private static int[] result = {-1};
    
    public int[] solution(int n, int[] info) {
        recurse(0, n, info);
        if (maxDiff > 0) {
            return result;
        }
        return new int[]{-1};
    }
    
    public static void recurse(int used, int total, int[] info) {
        if (used == total) {
            int diff = findDiff(info);
            if(maxDiff <= diff) {
                maxDiff = diff;
                result = cur.clone();
            }
            return;
        }
        
        for (int i=0; i<info.length && cur[i] <= info[i]; i++) {
            cur[i] += 1;
            recurse(used+1, total, info);
            cur[i] -= 1;
        }
    }

    public static int findDiff(int[] info) {
        int ryan = 0;
        int apeach = 0;
        for (int i=0; i < info.length; i++ ) {
            if(info[i] >= cur[i]) {
                if(info[i] != 0) {
                    apeach += 10 - i;
                }
            }
            else {
                ryan += 10 - i;
            }
        }
        return (ryan - apeach);
    }
}