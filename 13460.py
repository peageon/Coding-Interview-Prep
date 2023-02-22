import sys

N, M = map(sys.stdin.readline().split())
board = []
rx, ry, bx, by = 0,0,0,0
#Left, Up, Right, Down
dx = [-1,0,1,0]
dy = [0,-1,0,1]
#input board and find R and B coordinate
def get_board():
    for i in range(N):
        temp = []
        count = 0
        for x in sys.stdin.readline().strip():
            if x == 'R':
                rx, ry = i, count
            if x == 'B':
                bx, by = i, count
            count += 1
        board.append(temp)

def bfs():
    get_board()
    