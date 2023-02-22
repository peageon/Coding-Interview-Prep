#http://www.boj.kr/12865
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = []
for i in range(N):
    W, V = map(int, input().split())
    items.append((W,V))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        W, V = items[i-1]
        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], V + dp[i-1][j-W])

print(dp[N][K])
