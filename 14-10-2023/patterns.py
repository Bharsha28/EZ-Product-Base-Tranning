n=int(input())
s=n-1
e=n-1
for i in range(n):
    print("  "*(n-1-i)+"* "*i+"* "+"* "*(i))
for i in range(n):
    for j in range(2*n-1):
        if j>=s and j<=e:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    s-=1
    e+=1
    print()   
for i in range(n):
    for j in range(n):
        if i==j or j+i==n-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
for i in range(n):
    for j in range(n):
        if i==j or j+i==n-1:
            print(" ",end=" ")
        elif i==0 or i==n-1 or j==0 or j==n-1:
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()