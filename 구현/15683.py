import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = []

camera = [] #(x,y,camera_mode)
camera_mode = [
    [],
    [[0],[1],[2],[3]],
    [[1,3],[0,2]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

#    북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(m):
        if 0 < temp[j] < 6:
            camera.append((i, j, temp[j]))
    table.append(temp)

def fill_visible(graph, mode, x, y):
    for mo in mode:
        temp_x = x + dx[mo]
        temp_y = y + dy[mo]
        while 0 <= temp_x < n and 0 <= temp_y < m:
            if graph[temp_x][temp_y] == 0:
                graph[temp_x][temp_y] = 7
            elif graph[temp_x][temp_y] == 6:
                break
            temp_x = temp_x + dx[mo]
            temp_y = temp_y + dy[mo]
        

def counter(graph):
    count = 0
    for i  in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count
def dfs(graph, depth):
    global sol
    if depth == len(camera):
        sol = min(sol, counter(graph))
        return
    
    x, y, mode = camera[depth]
    for i in camera_mode[mode]:
        graph_copy = copy.deepcopy(graph)
        fill_visible(graph_copy, i, x, y)
        dfs(graph_copy, depth+1)
    

sol = int(1e9)
dfs(table, 0)
print(sol)