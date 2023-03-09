class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        if n == 3:
            return 5
        dp = [0] * (n+1)
        dp[1], dp[2], dp[3] = 1, 2, 5
        for i in range(4, n+1):
            dp[i] = dp[i-1] * 2 + dp[i-3]
        return dp[n] % (10**9 + 7)