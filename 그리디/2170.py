#선 긋기
import sys
input = sys.stdin.readline

N = int(input())

points = [tuple(map(int,input().split())) for _ in range(N)]
points.sort(key= lambda x: x[0])

left = points[0][0]
right = points[0][1]
sol = 0
for i in range(1,N): 
    x, y = points[i]
    if right >= x:
        right = max(y, right)
    else:
        sol += (right-left)
        left = x
        right = y
sol += (right-left)
print(sol)
