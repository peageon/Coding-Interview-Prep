def solve(n, graph):
    def dfs(u):
        nonlocal finish_time, visited
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        finish_time[u] = len(finish_time)
    
    graph = {i: [] for i in range(n)}
    for i, v in enumerate(graph):
        if supervisor[i] == -1:
            root = i
        else:
            graph[supervisor[i]].append(i)
    
    finish_time = [0] * n
    visited = [False] * n
    dfs(root)
    
    finish_time_sorted = sorted(range(n), key=lambda x: finish_time[x])
    
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        u = finish_time_sorted[i]
        dp[i] = dp[finish_time.index(min(finish_time[v] for v in graph[u]))] + 1
    
    minimum_time = max(dp)
    maximum_fire = n - minimum_time
    
    return minimum_time, maximum_fire

if __name__ == "__main__":
    n = int(input().strip())
    supervisor = [int(input().strip()) for _ in range(n)]
    minimum_time, maximum_fire = solve(n, supervisor)
    print(minimum_time)
    print(maximum_fire)