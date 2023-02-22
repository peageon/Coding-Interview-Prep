import sys
input = sys.stdin.readline

n, s = map(int,input().split())
nums = list(map(int, input().split()))
count = 0
cur = 0
def helper(x):
    global n, s, nums, count, cur
    if x == n and cur == s:
        count += 1
    if x < n:
        cur = cur + nums[x]
        helper(x+1)
        cur = cur - nums[x]
        helper(x+1)

helper(0)
if (s == 0):
    count -= 1
print(count)