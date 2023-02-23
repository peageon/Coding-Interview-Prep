#그림
import collections
import sys
input = sys.stdin.readline

N,M = map(int, input().split())

table = []
num_art = 0
width = 0

d = [(0,-1),(1,0),(0,1),(-1,0)]

for i in range(N):
    table.append(list(map(int, input().split())))

def bfs(i, j):
    global num_art, table, width
    queue = collections.deque()
    queue.append((i,j))
    temp_width = 0
    while queue:
        x, y = queue.popleft()
        if (table[x][y] == 1):
            table[x][y] = 0
            temp_width += 1
            for direction in d:
                x_prime, y_prime = direction
                temp_x = x + x_prime
                temp_y = y + y_prime
                if 0 <= temp_x < N and 0 <= temp_y < M and table[temp_x][temp_y] == 1:
                    queue.append((temp_x,temp_y))
        
    num_art += 1
    width = max(temp_width, width)


for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            bfs(i,j)
print(num_art)
print(width)