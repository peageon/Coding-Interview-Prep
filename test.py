T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    line = input().strip()
    count = 0
    cur = 97
    for letter in line:
        if ord(letter) == cur:
            count += 1
        cur += 1
    print('#'+test_case, count)