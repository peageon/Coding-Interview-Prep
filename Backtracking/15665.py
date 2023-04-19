from itertools import product
N, M = map(int, input().split())
j = sorted(set(map(int,input().split())))

for c in product(j, repeat=M):
    print(*c)