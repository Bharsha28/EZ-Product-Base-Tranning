n=list(map(int,input().split(" ")))
for i in range(1,len(l)):
    key=l[i]
    j=j-1
    while(j>=0 and l[j]>key):
        l[j+1]=l[j]
        j=j-1
    a[j+1]=key
print(l)