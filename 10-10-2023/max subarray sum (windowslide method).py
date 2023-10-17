l=list(map(int,input().split()))
tar=int(input())
sub=[]
for i in range(len(l)):
        for j in range(i + 1, len(l) + 1):
            sub.append(l[i:j])
max1=0
sum1=0
for i in range(len(sub)):
    if len(sub[i])==tar:
        sum1=sum(sub[i])
        if sum1>max1:
            max1=sum1
print(sum1)
        