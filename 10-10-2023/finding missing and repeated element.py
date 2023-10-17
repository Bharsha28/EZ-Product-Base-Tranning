'''n=int(input())
l=list(map(int,input().split()))[:n]
m=max(l)
res=((m*(m+1))//2)-sum(l)
print(res)'''
'''temp=0
ans=0
ans1=0
for i in range(1,n+1):
    for j in range(i+1,n):
        ans=l[i]^l[j]
        if ans==0:
            print(l[i])
    temp=temp^i
    ans1=ans1^l[i]
#print(temp)
res=temp^ans1
print(res)
print((4^6^6^5^7))'''
n=int(input())
arr=list(map(int,input().split()))
hashmap={}
#print(hashmap)
m=len(arr)
#Method - 1
print("Method - 1:- \n")
for i in range(m):
    if arr[i] not in hashmap:
        hashmap[arr[i]]=1
    else:
        hashmap[arr[i]]+=1
for i in range(1,n+1):
    if i not in hashmap:
        print(f"Missing Element is:- {i}")
    elif hashmap[i]>1:
        print(f"Repeated Element is:- {i}\n")
#Method - 2
print("Method - 2:- ")
s=set(arr)
miss=0
for i in s:
    miss^=i
for i in range(1,n+1):
    print(miss)
    miss^=i
repeat=0
for i in arr:
    repeat^=i
for i in s:
    repeat^=i
print(f"Missing Element is:- {miss}")
print(f"Repeated Element is:- {repeat}")