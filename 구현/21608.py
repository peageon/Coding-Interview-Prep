n = int(input())
table = [[0]*n for _ in range(n)]
#동서남북
neighbours = [(0,1),(0,-1),(1,0),(-1,0)]

def helper(s, l):
    temp_positions = check_first(l)
    if len(temp_positions) == 1:
        x, y = temp_positions[0]
    else:
        temp_positions = check_second(temp_positions) #check for temp_positions len 0
        x, y = check_third(temp_positions)
    table[x][y] = s
    return
    

def check_first(favs):
    global neighbours, n
    fav = 0
    res = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 0:
                neighbour_favs = 0
                for x, y in neighbours:
                    if 0<= i+x < n and 0 <= j+y < n and table[i+x][j+y] in favs:
                        neighbour_favs += 1
                if neighbour_favs > fav:
                    fav = neighbour_favs
                    res = []
                    res.append((i,j))
                elif neighbour_favs == fav:
                    res.append((i,j))
    return res

def check_second(poses):
    global neighbours
    if len(poses) == 0:
        fav = 0
        res = []
        for i in range(n):
            for j in range(n):
                if table[i][j] == 0:
                    empty = 0
                    for x, y in neighbours:
                        if 0<= i+x < n and 0 <= j+y < n and table[i+x][j+y] == 0:
                            empty += 1
                    if empty > fav:
                        fav = empty
                        res = []
                        res.append((i,j))
                    elif empty == fav:
                        res.append((i,j))
        return res
    else:
        fav = 0
        res = []
        for i,j in poses:
            if table[i][j] == 0:
                empty = 0
                for x, y in neighbours:
                    if 0<= i+x < n and 0 <= j+y < n and table[i+x][j+y] == 0:
                        empty += 1
                if empty > fav:
                    fav = empty
                    res = [(i,j)]
                elif empty == fav:
                    res.append((i,j))
        return res

def check_third(temp_positions):
    row = int(1e9)
    res = []
    for i,j in temp_positions:
        if i < row:
            res = [(i,j)]
        if i == row:
            res.append((i,j))
    if len(res) == 1:
        return res[0]
    
    return min(res, key=lambda x: x[1])


fav_dic = {}
for i in range(n**2):
    temp = list(map(int,input().split()))
    student = temp[0]
    likes = set(temp[1:])
    fav_dic[student] = likes
    helper(student, likes)

solution = 0
for i in range(n):
    for j in range(n):
        temp_temp = 0
        for x, y in neighbours:
            if 0<= i+x < n and 0 <= j+y < n and table[i+x][j+y] in fav_dic[table[i][j]]:
                temp_temp += 1
        if temp_temp > 0:
            solution += (10**(temp_temp-1))

print(solution)