n = int(input())
numbers = list(map(int,input().split()))
add, minus, mult, div = map(int,input().split())
maximum = -int(1e9)
minimum = int(1e9)
def dfs(i, cur):
    global n, numbers, add, minus, mult, div, maximum, minimum
    if i == n:
        maximum = max(maximum, cur)
        minimum = min(minimum, cur)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, cur + numbers[i])
            add += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, cur - numbers[i])
            minus += 1
        if mult > 0:
            mult -= 1
            dfs(i+1, cur * numbers[i])
            mult += 1
        if div > 0:
            div -= 1
            if cur < 0:
                dfs(i+1, (abs(cur) // numbers[i]) * -1)
            else:
                dfs(i+1, abs(cur) // numbers[i])
            div += 1
    return

dfs(1, numbers[0])
print(maximum)
print(minimum)