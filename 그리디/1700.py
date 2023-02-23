#멀티탭 스케줄링

def solution(n, k, arr):
    answer = 0
    multitap = []
    for i in range(k):
        if arr[i] in multitap:
            continue
        if len(multitap) < n:
            multitap.append(arr[i])
        else:
            idx = []
            for j in range(n):
                if multitap[j] in arr[i+1:]:
                    idx.append(arr[i+1:].index(multitap[j]))
                else:
                    idx.append(101)
            multitap[idx.index(max(idx))] = arr[i]
            answer += 1
    return answer

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(n, k, arr))