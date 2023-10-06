l=list(map(int,input().split(" ")))
for i in range(len(l)):
    c=0
    for j in range(len(l)-i-1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
            c+=1
            print(c)
    if c==0:
       print(l)
       break