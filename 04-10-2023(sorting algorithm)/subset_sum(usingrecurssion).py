def subset(arr,sum1,i):
    if sum1==0:
        return 1
    if sum1<0:
        return 0
    if i==len(arr):
        return 0
    return subset(arr,sum1-arr[i],i+1)+subset(arr,sum1,i+1)
arr=list(map(int,input().split(",")))
n=int(input())
c=subset(arr,n,0)
if c==0:
    print("no solution")
else:
    print("solution") 
print("number of solutions",subset(arr,n,0))