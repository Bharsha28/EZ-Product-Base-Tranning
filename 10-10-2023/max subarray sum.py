l=list(map(int,input().split()))
#tar=int(input())
sub=[]
for i in range(len(l)):
        for j in range(i + 1, len(l) + 1):
            sub.append(l[i:j])
max1=-1000
sum1=0
for i in range(len(sub)):
    sum1=sum(sub[i])
    if sum1>max1:
            max1=sum1
print("maximum sub array",max1)
def kadanes(l):
    max1=float("-inf")
    csum=l[0]
    n=len(l)
    for i in range(1,n):
        if csum<0:
            csum=0
        if l[i]<0:
            max1=max(max1,csum+l[i])
        csum=csum+l[i]
    return max(max1,csum)
print("maximum sum of subarray",kadanes(l))
