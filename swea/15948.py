import collections

def bfs(current, dp, dpt, table, row, col):
    maximum = 1
    stack = set([])
    stack.add(table[current[0]][current[1]])
    queue = collections.deque([[current, stack]])
    #print(queue)
    while queue:
        #print(queue)
        vertex = queue.popleft()
        #print(vertex)
        cur_pos = vertex[0]
        cur_stack = vertex[1]
        #print(cur_pos)
        #print(dpt[cur_pos[0] * col + cur_pos[1]])
        if not (dpt[cur_pos[0] * col + cur_pos[1]] - cur_stack):
            maximum = max(len(cur_stack), maximum)
        sidequests = dp[cur_pos[0] * col + cur_pos[1]]
        for sidequest in sidequests:
            if not table[sidequest[0]][sidequest[1]] in cur_stack:
                copy_stack = cur_stack.copy()
                copy_stack.add(table[sidequest[0]][sidequest[1]])
                queue.append([sidequest, copy_stack])
    return maximum


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    X = [-1,0,1,0]
    Y = [0,-1,0,1]
    row, col = map(int, input().split())
    dp = [[] for i in range(row * col)]
    dpt = [set([]) for i in range(row * col)]
    table = []
    for _ in range(row):
        table.append([*input()])
        
    for r in range(row):
        for c in range(col):
            for i in range(4):
                x = r + X[i]
                y = c + Y[i]
                if 0 <= x < row and 0 <= y < col:
                    dp[r * col + c].append([x,y])
                    dpt[r * col + c].add(table[x][y])
    print(bfs([0,0], dp, dpt, table, row, col))