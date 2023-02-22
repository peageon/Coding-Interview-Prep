n, m = map(int, input().split())
used = [False] * 10
arr = [0] * 10
def helper(k):
    if k == m:
        for i in range(m):
            print(f"{arr[i]}", end=" ")
        print()

    for i in range(1, n+1):
        if not used[i]:
            arr[k] = i
            used[i] = True
            helper(k+1)
            used[i] = False
    
helper(0)