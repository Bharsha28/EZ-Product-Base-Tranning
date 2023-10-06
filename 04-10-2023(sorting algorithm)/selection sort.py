a=list(map(int,input().split(" ")))
for i in range(len(a)):
    minn=i
    for j in range(i+1,len(a)):
        if a[minn] > a[j]:
            minn=j
    a[i],a[minn]=a[minn],a[i]
        
print(a)