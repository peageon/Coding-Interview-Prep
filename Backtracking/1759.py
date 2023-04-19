from itertools import combinations
l, c = map(int, input().split())

letters = sorted(input().split())

for c in combinations(letters, l):
    temp = 0
    for s in c:
        if s in "aeiou":
            temp += 1
    if 1 <= temp <= l - 2:
        print(''.join(c))
