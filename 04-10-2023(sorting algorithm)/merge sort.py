def merge_sort(l1):
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
l1=list(map(int,input().split(" ")))
print("original list:",l1)
merge_sort(l1)
print(l1)

