n = int(input())

results = [0] * (1001)
# 1=SK 2=CY

results[1] = 1
results[2] = 2
results[3] = 1

for i in range(4, 1001):
  if results[i-1] == 2 or results[i-3] == 2:
    results[i] = 1
  else:
    results[i] = 2
if results[n] == 1:
  print('SK')
else:
  print('CY')