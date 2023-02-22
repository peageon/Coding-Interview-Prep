import sys

def dfs(current_sum, w, m, l):
    local_sum = current_sum
    if l:
        i = l[0]
        for ind in range(len(m) - len(l) + 1):
            local_sum = max(local_sum, dfs(current_sum + w[i-1][m[ind]-1], w, m[ind+1:], l[1:]))
    return local_sum

input = sys.stdin.readline

n, m, c = map(int, input().split())

w = []
for i in range(c):
    w.append(list(map(int, input().split())))

a_personalities = list(map(int, input().split()))
b_personalities = list(map(int, input().split()))
more_students = a_personalities
less_students = b_personalities
if len(a_personalities) < len(b_personalities):
    more_students = b_personalities
    less_students = a_personalities
print(dfs(0, w, more_students, less_students))

'''if len(l) == 1:
        for ind in range(len(m) - len(l) + 1):
            print(current_sum)
            current_sum = max(current_sum, current_sum + w[i-1][m[ind]-1])
        return current_sum'''