l=list(map(int,input().split()))[:6]
l1=list(map(int,input().split()))[:6]
l2=[]
for i in range(len(l)):
    for j in range(len(l1)):
        x=l[i]+l[j]
        l2.append(x)
max1=0
for i in range(len(l2)):
    n=l2.count(l2[i])
    if(n>max1):
        max1=n
print(max1)
        