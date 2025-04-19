def solution(diffs, times, limit):
    answer = -1
    left = 1
    right = 100000
    while left <= right:
        mid = (left + right) // 2
        tot = times[0]
        for i in range(1, len(diffs)):
            if diffs[i] <= mid:
                tot += times[i]
            else:
                tot += (diffs[i] - mid) * (times[i-1] + times[i]) + times[i]
        if (tot <= limit):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer