#미로 탐색
import sys
import collections
input = sys.stdin.readline

N, M = map(int, input().split())

table = []
for i in range(N):
    table.append(list(map(int,input().strip())))

d = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs():
    queue = collections.deque()
    queue.append((0,0,0))
    while queue:
        x, y, count = queue.popleft()
        # print(x,y)
        # print(table)
        if table[x][y] == 1:
            table[x][y] = count+1
            for direction in d:
                dx, dy = direction
                temp_x = x + dx
                temp_y = y + dy
                if temp_x == N-1 and temp_y == M-1:
                    return count+2
                if 0 <= temp_x < N and 0 <= temp_y < M and (table[temp_x][temp_y] == 1 or count < table[temp_x][temp_y]):
                    queue.append((temp_x,temp_y,count+1))
    
sol = bfs()
print(sol)