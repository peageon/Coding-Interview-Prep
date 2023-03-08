c,s,n=0,0,int(input())
for i in range(1,n+1):
    s+=i
    c+=1
    if s>=n:
        print(c) if s==n else print(c-1)
        exit()
