T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    temp = list(map(int, input().split()))
    total = temp[0]
    nums = temp[1:]

    dp = [1] * total

    for i in range(1,total):
        for j in range(0, i):
            if nums[j] < nums[i]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
    print(f"#{test_case} {max(dp)}")