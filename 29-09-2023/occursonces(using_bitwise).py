l=list(map(int,input().split(" ")))
res=l[0]
for i in range(1,len(l)):
    res=res^l[i]
print(res)
