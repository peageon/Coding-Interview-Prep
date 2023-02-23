#ATM

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))
P.sort()
total = 0
sol = 0
for p in P:
    total += p
    sol += total

print(sol)