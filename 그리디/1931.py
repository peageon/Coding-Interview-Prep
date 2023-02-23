#회의실 배정

import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))
meetings.sort(key=lambda x: (x[1], x[0]))

used = 0
end = 0
for meeting in meetings:
    if meeting[0] >= end:
        used += 1
        end = meeting[1]

print(used)