n = int(input())
direction = [(0,1),(-1,0),(0,-1),(1,0)]
table = [[0] * 101 for _ in range(101)]
count =0

for i in range(n):
    y, x, d, g = map(int, input().split())
    table[x][y] = 1
    temp = []
    temp.append(d)
    dx, dy = direction[d]
    x, y = x+dx, y+dy
    table[x][y] = 1
    for _ in range(g):
        temptemp = temp[::-1]
        for p in temptemp:
            move = (p + 1) % 4
            dx, dy = direction[move]
            x, y = x+dx, y+dy
            table[x][y] = 1
            temp.append(move)
    
for i in range(100):
    for j in range(100):
        if table[i][j] and table[i][j+1] and table[i+1][j] and table[i+1][j+1]:
            count += 1
print(count)
