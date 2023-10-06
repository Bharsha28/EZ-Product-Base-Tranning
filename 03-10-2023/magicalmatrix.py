n=int(input())
l=[[0 for i in range(n)]
   for j in range(n)]
c=1
i=0
j=n//2
while c<=n*n:
       if i==-1 and j==n:
           i+=2
           j-=1
       else:
           if i==-1:
               i=n-1
           if j==n:
                j=0
       if l[i][j]:
           i+=2
           j-=1
           continue
       else:
           l[i][j]=c
           print(c,i,j)
           c+=1
       i-=1
       j+=1
for i in range(0,n):
    for j in range(0,n):
        print(l[i][j],end=" ")
    print()