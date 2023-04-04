N, L = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]



def helper(path):
    i = 0
    j = 1
    while j < N:
        if path[j] < path[i] - 1:
            return False
        elif path[j] == path[i] - 1:
            temp = path[j]
            for k in range(1,L):
                if j+k >= N or path[j+k] != temp:
                    return False
            i = j+(L-1)
            j = i + 1
            for k in range(L):
                if j+k >= N:
                    break
                if path[j+k] > path[i]:
                    return False
        else:
            i = j
            j += 1
    return True

def check_both(path):
    return helper(path) and helper(list(reversed(path)))


path_count = 0

for i in range(N):
    cur = []
    for j in range(N):
        cur.append(board[j][i])
    if check_both(cur):
        path_count += 1
    cur = board[i]
    if check_both(cur):
        path_count += 1

print(path_count)
    
    

