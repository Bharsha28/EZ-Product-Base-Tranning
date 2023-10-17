l=list(map(int,input().split()))
target=int(input())
l.sort()
i=0
j=len(l)-1
c=0
while i<j:
    if(l[i]+l[j]==target):
        print(i+1,"",j+1)
        c+=1
        break
    elif l[i] +l[j]>target:
        j-=1
    else:
        i+=1
if c==0:
    print("pair not found")