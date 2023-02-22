import sys
import collections
import time

input = sys.stdin.readline

n, m = map(int,input().split())

visited = [[0] * m for _ in range(n)]
table = []
x_list = [-1, 0, 1, 0]
y_list = [0, 1, 0, -1]

start_time = time.time()

count = 0
queue = collections.deque()
for i in range(n):
    table.append(list(map(int,input().split())))

for x in range(n):
    for y in range(m):
        if table[x][y] == 0:
            if visited[x][y] == 0:
                count += 1
                queue.append((x,y))
                while queue:
                    #USE DFS FOR SHORTER TIME
                    a, b = queue.popleft()
                    visited[a][b] = 1
                    for i in range(4):
                        temp_x = a + x_list[i]
                        temp_y = b + y_list[i]

                        if (temp_x < 0):
                            temp_x = n - 1
                        elif (temp_x > n - 1):
                            temp_x = 0
                        
                        if (temp_y < 0):
                            temp_y = m - 1
                        elif (temp_y > m - 1):
                            temp_y = 0

                        if (table[temp_x][temp_y] == 0 and visited[temp_x][temp_y] == 0):
                            queue.append((temp_x, temp_y))

print(time.time() - start_time)
print(count)
