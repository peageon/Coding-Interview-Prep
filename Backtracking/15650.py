from collections import deque

N, M = map(int, input().split())
array = deque()

def dfs(d):
    if d == M:
        print(*array)
    else:
        temp = 0
        if array:
            temp = array[-1]
        for i in range(temp + 1, N - M + d + 2):
            array.append(i)
            dfs(d+1)
            array.pop()

dfs(0)