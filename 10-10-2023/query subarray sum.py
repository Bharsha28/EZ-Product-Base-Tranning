n=list(map(int,input().split()))
m=int(input("Enter length of query"))
l=[]
for i in range(m):
    start,end=list(map(int,input().split()))
    l.append([start,end])
i=0
j=0
l1=[]
while (i<=len(l)):
    a=l[i][j]
    j+=1
    b=l[i][j]
    sum1=0
    for i in range(a,b):
        sum1+=n[i]
        l1.append(sum1)
    i+=1
    j=0
print(l1)
