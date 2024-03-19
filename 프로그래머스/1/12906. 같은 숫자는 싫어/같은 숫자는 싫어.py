def solution(arr):
    cur = -1
    new_list = list()
    for element in arr:
        if element != cur:
            new_list.append(element)
        cur = element
    return new_list