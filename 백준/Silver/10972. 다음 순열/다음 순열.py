n = int(input())
nums = list(map(int, input().split()))
for i in range(n-1, 0, -1):
  if nums[i] > nums[i-1]:
    for j in range(n-1, i-1, -1):
      if nums[i-1] < nums[j]:
        nums[j], nums[i-1] = nums[i-1] , nums[j]
        temp = nums[:i] + sorted(nums[i:])
        print(*temp)
        exit()
print(-1)