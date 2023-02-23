#보물

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

B.sort(reverse=True)
A.sort()

total = 0
for i in range(N):
    total += (A[i] * B[i])

print(total)