n = int(input())

dp = [0] * (n+2)
for i in range(1, n+1):
    t, p = map(int,input().split())
    j = i + t
    while j <= n+1:
        if dp[j] < dp[i] + p:
            dp[j] = dp[i] + p
        j += 1
print(dp[-1])
    