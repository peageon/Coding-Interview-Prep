from collections import deque
import copy
N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]

#완전 탐색
#3개의 벽을 임의로 세우고 bfs를 통해서 안전영역의 값을 구한다
#모든 경우의수에 반복
#최댓값 리턴
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    #breadth first search
    board_copy = copy.deepcopy(board)
    queue = deque()
    for i in range(N):
        for j in range(M):
            if board_copy[i][j] == 2:
                queue.append((i,j))
    
    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            if 0 <= i + dy[direction] < N and 0 <= j + dx[direction] < M and board_copy[i + dy[direction]][j + dx[direction]] == 0:
                board_copy[i + dy[direction]][j + dx[direction]] = 3
                queue.append((i + dy[direction], j + dx[direction]))
    
    total = 0
    for i in range(N):
        for j in range(M):
            if board_copy[i][j] == 0:
                total += 1
    return total

def make_wall(count_wall):
    global safe_zone
    if count_wall == 3:
        temp = bfs()
        if temp > safe_zone:
            safe_zone = temp
        return
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(count_wall+1)
                board[i][j] = 0

safe_zone = 0
make_wall(0)
print(safe_zone)