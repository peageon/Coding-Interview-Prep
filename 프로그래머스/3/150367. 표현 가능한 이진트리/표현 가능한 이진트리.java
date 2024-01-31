import java.lang.Math;
class Solution {
    public int[] solution(long[] numbers) {
        int[] result = new int[numbers.length];
        for(int i=0; i<numbers.length; i++) {
            long num = numbers[i];
            int validity = check(num);
            result[i] = validity;
        }
        return result;
    }
    
    public static int check(long num) {
        String bin = Long.toBinaryString(num);
        int j = 0;
        while(Math.pow(2, j) - 1 < bin.length()) {
            j++;
        }
        bin = "0".repeat((int)Math.pow(2, j) - 1 - bin.length()) + bin;
        if(dfs(bin)) {
            return 1;
        }
        return 0;
    }
    
    public static boolean dfs(String bin) {
        int mid = (bin.length()-1) /2;
        char root = bin.charAt(mid);
        String left = bin.substring(0, mid);
        String right = bin.substring(mid+1, bin.length());
        if(root == '0') {
            if(left.charAt((left.length()-1)/2) == '1' || right.charAt((right.length()-1)/2) == '1') {
                return false;
            }
        }
        
        if(left.length() >= 3) {
            if(!dfs(left)) {
                return false;
            }
            if(!dfs(right)) {
                return false;
            }
        }
        return true;
    }
}