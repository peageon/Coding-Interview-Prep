from itertools import combinations
n, m = map(int,input().split())
home = []
kfc = []

sol = int(1e9)

for i in range(n):
    for j, s in enumerate(list(map(int,input().split()))):
        if s == 1:
            home.append((i,j))
        elif s == 2:
            kfc.append((i,j))

for comb in combinations(kfc, m):
    temp_tot_d = 0
    for r, c in home:
        temp_d = int(1e9)
        for x, y in comb:
            temp_d  = min(temp_d, abs(x-r) + abs(y-c))
        temp_tot_d += temp_d
    sol = min(sol, temp_tot_d)

print(sol)
