import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

B = []

for i in range(H+X):
    B.append(list(map(int, input().split())))

#A = []
for i in range(H):
    for j in range(W):
        x_calc, y_calc = i - X, j - Y
        #if x_calc < 0 or y_calc < 0:
        if 0 <= x_calc < H and 0 <= y_calc < W:
            B[i][j] = B[i][j] - B[x_calc][y_calc]
            print(B[i][j], end=" ")
        else:
            print(B[i][j], end=" ")
    print()
    #A.append(temp)

#print(A)
