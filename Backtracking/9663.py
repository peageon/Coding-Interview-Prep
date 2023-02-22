#1<= N <= 15

n = int(input())

col = [False] * n
increasing_diagonal = [False] * (n * 2 - 1)
decreasing_diagonal = [False] * (n * 2 - 1)
count = 0


def helper(cur):
    global col, increasing_diagonal, decreasing_diagonal, n, count
    if cur == n:
        count += 1
    
    for i in range(n):
        if not (col[i] or increasing_diagonal[cur + i] or decreasing_diagonal[cur - i]):
            col[i] = True
            increasing_diagonal[cur + i] = True
            decreasing_diagonal[cur - i] = True
            helper(cur+1)
            col[i] = False
            increasing_diagonal[cur + i] = False
            decreasing_diagonal[cur - i] = False


helper(0)
print(count)