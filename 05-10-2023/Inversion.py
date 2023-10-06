l1=list(map(int,input().split()))
#time complexity O(N^2)
'''count=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if i<j:
            if l[i]>l[j]:
                count+=1
print(count)'''
#optimalized code of time complexcity O(Nlog(N))
def merge_sort(l1):
    global c
    if(len(l1)<=1):
        return l1
    else:
        mid=len(l1)//2
        left=l1[:mid]
        right=l1[mid:]
        merge_sort(left)
        merge_sort(right)
        i=0
        j=0
        k=0
        while(i <len(left) and j<len(right)):
           if(left[i]<=right[j]):
               l1[k]=left[i]
               i+=1
               k+=1
           else:
                l1[k]=right[j]
                c+=len(left)-i
                j+=1
                k+=1
        while(i <len(left)):
            l1[k]=left[i]
            i+=1
            k+=1
        while(j <len(right)):
            l1[k]=right[j]
            j+=1
            k+=1
    return c
print("original list:",l1)
c=0
print(merge_sort(l1))