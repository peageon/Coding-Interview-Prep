import sys
import collections
input = sys.stdin.readline

n, m, v = map(int, input().split())

visited_bfs = [False] * 1001
visited_dfs = [False] * 1001
connections = [[] for _ in range(n + 1)]
queue = collections.deque()
for i in range(m):
    a, b = map(int, input().split())

    connections[a].append(b)
    connections[b].append(a)

def dfs(start):
    global visited_dfs
    print(start, end=" ")
    for connecting_element in sorted(connections[start]):
        if visited_dfs[connecting_element] == False:
            visited_dfs[connecting_element] = True
            dfs(connecting_element)

def bfs(start):
    global visited_bfs
    queue.append(start)
    while queue:
        cur = queue.popleft()
        print(cur, end=" ")
        for connection in sorted(connections[cur]):
            if not visited_bfs[connection]:
                visited_bfs[connection] = True
                queue.append(connection)

visited_dfs[v] = True
dfs(v)
print()

visited_bfs[v] = True
bfs(v)
print()