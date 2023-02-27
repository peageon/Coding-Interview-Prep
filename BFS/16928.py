#뱀과 사다리 게임
from collections import deque

N, M = map(int, input().split())
dice = [1,2,3,4,5,6]
table = [i for i in range(101)]
visited = [101] * 101
# print(visited)

#ladder
for _ in range(N):
    x, y = map(int, input().split())
    table[x] = y

#snake
for _ in range(M):
    u, v = map(int, input().split())
    table[u] = v

q = deque()
#(current_location, moves_made)
q.append((1,0))
while q:
    cur, moves = q.popleft()

    for num in dice:
        if cur + num < 100 and visited[table[cur+num]] > moves+1:
            visited[table[cur+num]] = moves+1
            q.append((table[cur+num], moves+1))
        elif cur + num == 100:
            print(moves+1)
            exit()
        else:
            continue