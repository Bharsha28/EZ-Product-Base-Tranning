n=int(input())
m=int(input())
l=[]
for i in range(n):
    l1=[]
    for j in range(m):
        a=int(input())
        l1.append(a)
    l.append(l1)
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j],end=" ")
    print()
for i in range(n):
    for j in range(m-1,-1,-1):
            print(l2[j][i],end=" ")
    print()
for i in range(n-1,-1,-1):
    for j in range(m):
            print(l2[j][i],end=" ")
    print()            
            
         
       
