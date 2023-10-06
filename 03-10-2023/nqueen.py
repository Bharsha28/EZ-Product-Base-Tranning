n=int(input())
l=[[0 for i in range(n)]
   for j in range(n)]
c=1
i=0
j=1
if n<=3:
    print("invalid input")
else:
    while c<=n:
        if j>=n:
            j=0
        l[i][j]=c
        c+=1
        i+=1
        j+=2
    for i in range(0,n):
        for j in range(0,n):
            print(l[i][j],end=" ")
        print()