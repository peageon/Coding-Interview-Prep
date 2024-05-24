def solve():
  char_dict = {'B':'O','O':'J','J':'B'}

  n = int(input())
  boj = list(input())
  dp = [None for _ in range(n)]
  dp[0] = 0

  for i in range(0,n-1):
    cur_char = boj[i]
    next_char = char_dict[cur_char]
    if dp[i] == None:
      continue
    for j in range(i+1, n):
      if boj[j] == next_char:
        cost = (dp[i] + (j-i)**2)
        if dp[j] == None or cost < dp[j]:
          dp[j] = cost
  if dp[-1] == None:
    print(-1)
  else:
    print(dp[-1])

solve()