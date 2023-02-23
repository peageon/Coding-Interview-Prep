#벽 부수기
#boj.kr/2206

#WRONG
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# table = [list(map(int, input().strip())) for _ in range(N)]
# visited = [[[0] * M for _ in range(N)]] * 2


# d = [(1,0),(0,1),(-1,0),(0,-1)]
# q = []
# q.append((0,0,True,1))
# moves = int(1e9)
# for j in q:
#     x, y, destroy, move = j
#     level = 1
#     if not destroy:
#         level = 0
#     if table[x][y] == 0 or (level == 1 and visited[level][x][y] == 0):
#         visited[level][x][y] = 1
#         if table[x][y] == 1:
#             level = 0
#         visited[level][x][y] = 1
#         for direction in d:
#             dx, dy = direction
#             tempx = x + dx
#             tempy = y + dy
#             if tempx == N - 1 and tempy == M - 1:
#                 moves = min(moves, move+1)
#                 continue
#             if 0 <= tempx < N and 0 <= tempy < M:
#                 if visited[level][tempx][tempy] == 0 and table[tempx][tempy] == 1 and bool(level):
#                     q.append((tempx,tempy, bool(level), move+1))
#                 elif table[tempx][tempy] == 0 and visited[level][tempx][tempy] == 0:
#                     q.append((tempx, tempy, bool(level), move+1))
# print(moves if moves < 1000001 else -1)
        