from collections import defaultdict
def solution(edges):
    result = [0,0,0,0]
    all_keys = set()
    def add_result(index):
        result[index] += 1
    middle = -1
    num_graphs = 0
    incoming = defaultdict(list)
    outgoing = defaultdict(list)
    for out, inn in edges:
        incoming[inn].append(out)
        outgoing[out].append(inn)
        all_keys.add(inn)
        all_keys.add(out)
    
    for key in all_keys:
        if len(outgoing[key]) == 2:
            if not incoming[key]:
                middle = key
                num_graphs = len(outgoing[key])
                result[0] = middle
            else:
                add_result(3)
        elif len(outgoing[key]) == 0:
            add_result(2)
        elif len(outgoing[key]) > 2:
            middle = key
            num_graphs = len(outgoing[key])
            result[0] = middle
    
    result[1] = num_graphs - result[2] - result[3]
    return result
        
        