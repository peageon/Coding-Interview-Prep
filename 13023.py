import sys
input = sys.stdin.readline

n, m = map(int,input().split())

the_list = [[] for _ in range(n)]
visited = [0] * 2001

for i in range(m):
    a, b = map(int,input().split())

    the_list[a].append(b)
    the_list[b].append(a)

def dfs(element, depth):
    if depth == 5:
        print(1)
        exit()
    
    for i in the_list[element]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False

print(0)