l=[15,5,22,40,60,51]
l1=[20,10,30,50]
l.sort()
l1.sort()
l3=[]
i=0
j=0
while i<len(l) and j<len(l):
    if i>=len(l):
        while j<len(l1):
            l3.append(l1[j])
            j+=1
    elif  j>=len(l1):
          while i<len(l):
            l3.append(l[i])
            i+=1
    elif l[i]>l1[j]:
        l3.append(l1[j])
        j+=1
    else: 
        l3.append(l[i])
        i+=1 
print(l3)