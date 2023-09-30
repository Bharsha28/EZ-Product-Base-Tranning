def linearser(l,ser):
    c=0
    for i in range(len(l)):
        if(l[i]==ser):
            c+=1
            break
    if(c>=1):
       return True
    else:
        return False
n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
ser=int(input("Enter element to search"))
res=linearser(l,ser)
if res is True:
    print("Element found ")
else:
    print("Element not found")