k = int(input())
array = []
for _ in range(k):
    array.extend(list(map(int, input().split())))
d = [0] * k * 3

d[0],d[1],d[2] = array[0],array[1],array[2]

for i in range(3, k*3):
    if i % 3 == 0:
        d[i] = min(d[i-2], d[i-1]) + array[i]
    elif i % 3 == 1:
        d[i] = min(d[i-4], d[i-2]) + array[i]
    else:
        d[i] = min(d[i-5], d[i-4]) + array[i]
    
print(min(d[-1],d[-2],d[-3]))