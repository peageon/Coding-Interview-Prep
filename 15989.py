test_cases = int(input())

table = [1] * 10001

for i in range(2, 10001):
    table[i] += table[i-2]
for i in range(3, 10001):
    table[i] += table[i-3]

for _ in range(test_cases):
    sol = int(input())
    print(table[sol])