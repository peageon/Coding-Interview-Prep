N = int(input())

numbers = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]

for add in range(N):
    for start in range(N - add):
        end = start + add
        if start == end:
            dp[start][end] = 1
        elif numbers[start] == numbers[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

num_questions = int(input())

for _ in range(num_questions):
    start, end = map(int, input().split())
    print(dp[start-1][end-1])