import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
cities = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    cities[a].append(b)

results = []

que = deque()
que.append((x, 0))
visited[x] = True

while que:
    city, distance = que.popleft()
    if distance == k:
        results.append(city)
        continue

    for c in cities[city]:
        if not visited[c]:
            visited[c] = True
            que.append((c, distance+1))

results.sort()
if not results:
    print(-1)
else:
    print(*results)