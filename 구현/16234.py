from collections import deque
n,l,r = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
dp = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x, y):
    union = []
    tot = 0
    queue = deque([(x,y)])
    while queue:
        i,j = queue.popleft()
        if (visit[i][j]):
            continue
        tot += table[i][j]
        visit[i][j] = True
        union.append((i,j))
        for dx, dy in dp:
            cx, cy = i+dx, j+dy
            if 0 <= cx < n and 0 <= cy < n and l <= abs(table[cx][cy] - table[i][j]) <= r and visit[cx][cy] == False:
                queue.append((cx,cy))
    avg = tot // len(union)
    for i, j in union:
        table[i][j] = avg
    return len(union)

count = 0
while True:
    visit = [[False] * n for _ in range(n)]
    sol = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False:
                if bfs(i,j) > 1:
                    sol = True
    if sol:
        count += 1
    else:
        break
print(count)