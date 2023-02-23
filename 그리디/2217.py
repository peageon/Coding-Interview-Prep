import sys
input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort()
total = 0
maximum = 0
used = 0
for rope in reversed(ropes):
    if used == 0:
        total += rope
        maximum += rope
        used += 1
    else:
        total = total + rope
        temp = total / (used+1)
        if temp > rope:
            temp = rope
        if temp * (used+1) > maximum:
            maximum = temp * (used+1)
        used += 1
print(maximum)