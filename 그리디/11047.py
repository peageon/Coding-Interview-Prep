#동전 0
#boj.kr/11047

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
used = 0
for coin in reversed(coins):
    temp = K // coin
    if temp == 0:
        continue
    else:
        K = K % coin
        used += temp

print(used)