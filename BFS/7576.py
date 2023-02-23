#토마토
import sys
import collections
input = sys.stdin.readline

M, N = map(int, input().split())
table = []
tomato = []
total_tomatoes = 0
d = [(1,0),(0,1),(-1,0),(0,-1)]

for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(M):
        if temp[j] == 1:
            total_tomatoes += 1
            tomato.append((i,j,0))
        elif temp[j] == 0:
            total_tomatoes += 1
    table.append(temp)


def bfs():
    ripe = 0
    days = 0
    queue = collections.deque(tomato)
    while queue:
        x, y, day = queue.popleft()
        if table[x][y] == 0 or day == 0:
            table[x][y] = 1
            ripe += 1
            days = day
            for direction in d:
                dx, dy = direction
                tempx = x + dx
                tempy = y + dy
                if 0 <= tempx < N and 0 <= tempy < M and table[tempx][tempy] == 0:
                    queue.append((tempx,tempy, day+1))
    if total_tomatoes - ripe == 0:
        return days
    else:
        return -1

if len(tomato) == total_tomatoes:
    print(0)
else:
    res = bfs()
    print(res)
        
            
