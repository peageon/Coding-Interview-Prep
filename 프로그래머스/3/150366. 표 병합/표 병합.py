cells = [["EMPTY"] * 51 for _ in range(51)]
parents = [[(r,c) for c in range(51)] for r in range(51)]
result = []

def find_parent(r, c):
    if (r,c) == parents[r][c]:
        return parents[r][c]
    pr, pc = parents[r][c]
    #압축
    parents[r][c] = find_parent(pr,pc)
    return parents[r][c]

def update(r, c, value):
    pr, pc = find_parent(r,c)
    cells[pr][pc] = str(value)

def update_all(val_one, val_two):
    for i in range(51):
        for j in range(51):
            if cells[i][j] == val_one:
                cells[i][j] = str(val_two)

def merge(r1, c1, r2, c2):
    pr1, pc1 = find_parent(r1, c1)
    pr2, pc2 = find_parent(r2, c2)
    if pr1 == pr2 and pc1 == pc2:
        return
    p2_val = cells[pr2][pc2]
    p1_val = cells[pr1][pc1]
    val = p1_val
    if p1_val == "EMPTY" and p2_val != "EMPTY":
        val = p2_val
        parents[pr1][pc1] = (pr2, pc2)
    else:
        cells[pr2][pc2] = "EMPTY"
        parents[pr2][pc2] = (pr1, pc1)
        
def unmerge(r, c):
    pr, pc = find_parent(r, c)
    value = cells[pr][pc]
    unmerge_list = []
    
    for i in range(51):
        for j in range(51):
            qr, qc = find_parent(i,j)
            if (qr,qc) == (pr, pc):
                unmerge_list.append((i,j))
    
    for (qr, qc) in unmerge_list:
        parents[qr][qc] = (qr, qc)
        if (qr, qc) == (r,c):
            cells[qr][qc] = value
        else:
            cells[qr][qc] = "EMPTY"
    
def print(r, c):
    pr, pc = find_parent(r, c)
    result.append(cells[pr][pc])
 
    
def solution(commands):
    for command in commands:
        args = command.split()
        if args[0] == "UPDATE" and len(args) == 4:
            update(int(args[1]), int(args[2]), args[3])
        elif args[0] == "UPDATE" and len(args) == 3:
            update_all(args[1], args[2])
        elif args[0] == "MERGE":
            merge(int(args[1]), int(args[2]), int(args[3]), int(args[4]))
        elif args[0] == "UNMERGE":
            unmerge(int(args[1]), int(args[2]))
        else:
            print(int(args[1]), int(args[2]))
    return result