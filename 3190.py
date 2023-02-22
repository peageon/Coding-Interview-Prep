import sys
from collections import deque

#우 하 좌 상
dx = [1,0,-1,0]
dy = [0,1,0,-1]

apples = set()
moves = deque([])
N = sys.stdin.readline().strip()
K = sys.stdin.readline().strip()
for i in range(int(K)):
    apples.add(tuple(sys.stdin.readline().split(" ")))
for k in range(int(sys.stdin.readline().strip())):
    moves.append(list(map(int, sys.stdin.readline().split())))

snake = deque([[1,1]])
def game(): 
    count = 0
    dir = 0
    for move in moves:
        for _ in range(move[0]-count):
            temp = snake[0].copy()
            temp[0] = temp[0] + dx[dir]
            temp[1] = temp[1] + dy[dir]
            if (temp in snake) or (not 0 < temp[1] < N+1) or (not 0 < temp[0] < N+1):
                return count
            if (tuple(temp) in apples):
                snake.appendleft(temp)
                apples.remove(tuple(temp))
            else:
                snake.appendleft(temp)
                snake.pop()
        change_dir(dir, move[1])
    return count

def change_dir(d, change):
    if change == "L":
        d = (d-1) %4
    else:
        d = (d+1) %4
    return d

print(game())