def solution(progresses, speeds):
    index = 0
    result = list()
    while index < len(progresses):
        tt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while index < len(progresses) and progresses[index] >= 100:
            tt += 1
            index += 1
        if tt:
            result.append(tt)
    return result