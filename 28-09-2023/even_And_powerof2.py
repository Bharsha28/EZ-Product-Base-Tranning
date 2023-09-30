n=int(input())
r1=int(input())
r2=int(input())
l=[]
for i in range(n):
    x=int(input())
    if(x>=r1 and x<=r2):
        l.append(x)
    else:
        print("Enter number with in range")
        y=int(input())
        l.append(y)
l1=[]
for i in range(len(l)):
    if(l[i]%2==0):
        l1.append(l[i])
print(l2)
print()
for i in l:
    for j in range(0,max(l1)):
        if(2**j==i):
            print(i)

    