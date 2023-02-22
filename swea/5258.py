#다이나믹 프로그래밍 3일차 부분집합의 합 
testcases = int(input())
for x in range(testcases):
    boxsize, itemcount = map(int, input().split())
    d = [0] * (boxsize +1)
    items = [list(map(int, input().split())) for _ in range(itemcount)]
    for item in items:
        for w in range(boxsize, 0, -1):
            if item[0] <= w:
                d[w] = max(d[w], d[w-item[0]]+item[1])
        print(*d)
    print(f'#{x+1} {d[boxsize]}')