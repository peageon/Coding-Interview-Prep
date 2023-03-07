#주사위 굴리기

n, m, x, y, k = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

moves = list(map(int,input().split()))
#       north, west, bottom, east, south, top
dice = [0,0,0,0,0,0]

def move_dice(dice, direction, board, x, y):
    #east
    if direction == 1:
        if y+1 >= len(board[0]):
            return (dice, board, x, y)
        y = y + 1
        temps = [dice[2],dice[3],dice[5],dice[1]]
        dice[1] = temps[0]
        dice[2] = temps[1]
        dice[3] = temps[2]
        dice[5] = temps[3]
    #west
    elif direction == 2:
        if y-1 < 0:
            return (dice, board, x, y)
        y = y - 1
        temps = [dice[5],dice[1],dice[2],dice[3]]
        dice[1] = temps[0]
        dice[2] = temps[1]
        dice[3] = temps[2]
        dice[5] = temps[3]
    #north
    elif direction == 3:
        if x - 1 < 0:
            return (dice, board, x, y)
        x = x - 1
        temps = [dice[5],dice[0],dice[2],dice[4]]
        dice[0] = temps[0]
        dice[2] = temps[1]
        dice[4] = temps[2]
        dice[5] = temps[3]
    #south
    elif direction == 4:
        if x + 1 >= len(board):
            return (dice, board, x, y)
        x = x + 1
        temps = [dice[2],dice[4],dice[5],dice[0]]
        dice[0] = temps[0]
        dice[2] = temps[1]
        dice[4] = temps[2]
        dice[5] = temps[3]

    if board[x][y] == 0:
        board[x][y] = dice[2]
    else:
        dice[2] = board[x][y]
        board[x][y] = 0
    print(dice[5])
    return (dice, board, x, y)


for move in moves:
    dice, board, x, y = move_dice(dice, move, board, x, y)