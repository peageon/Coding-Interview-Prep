#로봇 청소기

n,m = map(int, input().split())
r, c, d = map(int, input().split())

#북, 동, 남, 서
dd = [(-1,0),(0,1),(1,0),(0,-1)]

cleaned = 0
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

def clean(x, y, direction):
    global cleaned, board, n, m
    if board[x][y] == 0:
        board[x][y] = 2
        cleaned += 1
    blocked = True
    for dx,dy in dd:
        if board[x+dx][y+dy] == 0:
            blocked = False
    
    if blocked:
        back_direction = (direction + 2) % 4
        dx, dy = dd[back_direction]
        if board[x+dx][y+dy] != 1:
            return clean(x+dx, y+dy, direction)
        else:
            return False
    else:
        direction = (direction - 1) % 4
        dx, dy = dd[direction]
        while board[x+dx][y+dy] != 0:
            direction = (direction - 1) % 4
            dx, dy = dd[direction]
        return clean(x+dx, y+dy, direction)
    
clean(r, c, d)
print(cleaned)