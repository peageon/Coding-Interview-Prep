'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k+1)
for i in range(n):
    w, v = map(int, input().split())
    if v > dp[w]:
        dp[w] = v

for i in range(1,k):
    for j in range(i+1, k+1):
        new = dp[i] + dp[j - i]
        if dp[j] < new:
            dp[j] = new

print(dp[-1])
'''


n, k = map(int,input().split())

dp = [[0] * (k+1) for j in range(n+1)]

for i in range(1,n+1):
    weight, value = map(int, input().split())

    for j in range(1, k+1):

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][k])