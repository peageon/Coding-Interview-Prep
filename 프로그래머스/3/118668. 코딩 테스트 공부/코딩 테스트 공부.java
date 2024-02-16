class Solution {
    public static int solution(int alp, int cop, int[][] problems) {
        int targetAlp = 0;
        int targetCop = 0;

        for(int i=0; i < problems.length; i++) {
            targetAlp = Math.max(targetAlp, problems[i][0]);
            targetCop = Math.max(targetCop, problems[i][1]);
        }

        if(targetAlp <= alp) {
            alp = targetAlp;
        }
        if(targetCop <= cop) {
            cop = targetCop;
        }

        if(alp == targetAlp && cop == targetCop) {
            return 0;
        }

        int[][] dp = new int[targetAlp+2][targetCop+2];
        for(int i=alp; i <= targetAlp; i++) {
            for(int j=cop; j <= targetCop; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        dp[alp][cop] = 0;

        for(int i=alp; i <= targetAlp; i++) {
            for(int j=cop; j <= targetCop; j++) {
                dp[i+1][j] = Math.min(dp[i+1][j], dp[i][j] + 1);
                dp[i][j+1] = Math.min(dp[i][j+1], dp[i][j] + 1);

                for(int[] problem: problems) {
                    if(i >= problem[0] && j >= problem[1]) {
                        if(i+problem[2] > targetAlp && j+problem[3] > targetCop) {
                            dp[targetAlp][targetCop] = Math.min(dp[targetAlp][targetCop], dp[i][j] + problem[4]);
                        }
                        else if(i+problem[2] > targetAlp) {
                            dp[targetAlp][j+problem[3]] = Math.min(dp[targetAlp][j+problem[3]], dp[i][j] + problem[4]);
                        }
                        else if(j+problem[3] > targetCop) {
                            dp[i+problem[2]][targetCop] = Math.min(dp[i+problem[2]][targetCop], dp[i][j] + problem[4]);
                        }
                        else {
                            dp[i+problem[2]][j+problem[3]] = Math.min(dp[i+problem[2]][j+problem[3]], dp[i][j] + problem[4]);
                        }
                    }
                }
            }
        }
        return dp[targetAlp][targetCop];
    }
}