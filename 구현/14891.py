from collections import deque

bolt = []
turned = [0,0,0,0]

def turn(n, d):
    global bolt
    if d == -1:
        temp = bolt[n-1].popleft()
        bolt[n-1].append(temp)
    else:
        temp = bolt[n-1].pop()
        bolt[n-1].appendleft(temp)
    return

def helper(numb, direction):
    global bolt
    if turned[numb - 1] == 1:
        return
    else:
        turned[numb - 1] = 1
        if numb - 2 >= 0 and bolt[numb - 2][2] != bolt[numb - 1][6]:
            helper(numb - 1, direction * -1)
        if numb < 4 and bolt[numb][6] != bolt[numb - 1][2]:
            helper(numb + 1, direction * -1)
        turn(numb, direction)
        turned[numb - 1] = 0

for _ in range(4):
    temp = deque([int(x) for x in input()])
    bolt.append(temp)

turns = int(input())
for t in range(turns):
    numero, direc = map(int, input().split())
    helper(numero, direc)

total = 0
for i in range(4):
    total += bolt[i][0] * (2**i)

print(total)