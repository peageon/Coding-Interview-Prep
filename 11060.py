N = int(input())
table = [i for i in map(int,input().split())]
dp = [1001 for _ in range(N)]

dp[0] = 0

for i in range(N):
    bi = dp[i] + 1
    ai = table[i]
    for j in range(1,ai+1):
        if i+j <= N-1 and bi < dp[i+j]:
            dp[i+j] = bi

if dp[-1] < 1001:
    print(dp[-1])
else:
    print(-1)