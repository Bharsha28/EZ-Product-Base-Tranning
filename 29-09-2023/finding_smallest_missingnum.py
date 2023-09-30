'''l=list(map(int,input().split(",")))
l1=[]
for  i in range(0,max(l)+2):
    l1.append(i)
for i in l1:
    if(i not in l):
        print(i)
        break'''
l2=[]
n=int(input("Enter size"))
for i in range(n):
    x=int(input())
    l2=l2+[x]
for  i in range(0,max(l2)+2):
     if(i not in l2):
        print("missing value:",i)
        break

   