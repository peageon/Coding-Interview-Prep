#TIME OUT 
#TIME OUT
#TIM EOUT
import collections
import sys
def bfs(k, v, table):
    stack = collections.deque()
    visited = set()
    visited.add(v)
    minimum = sys.maxsize
    stack.append([v, visited, minimum])
    possible = dict()
    for key in table.keys():
        possible[key] = sys.maxsize
    while stack:
        item = stack.popleft()
        current = item[0]
        visited_vids = item[1]
        minim = item[2]
        for item in table[current]:
            vertex = item[0]
            cost = item[1]
            if vertex in visited_vids:
                continue
            else:
                jam = min(minim, cost)
                possible[vertex] = min(possible[vertex], jam)
                new_visited = visited_vids.copy()
                new_visited.add(vertex)
                stack.append([vertex, new_visited, jam])
    count = 0
    for value in possible.values():
        if k <= value < sys.maxsize:
            count += 1
            
    return count

N, Q = map(int, input().split())
table = dict()
for i in range(N-1):
    p, q, r = map(int, input().split())
    if p in table:
        table[p].append([q, r])
    else:
        table[p] = [[q,r]]
    if q in table:
        table[q].append([p, r])
    else:
        table[q] = [[p,r]]

for i in range(Q):
    k, v = map(int,input().split())
    print(bfs(k, v, table))