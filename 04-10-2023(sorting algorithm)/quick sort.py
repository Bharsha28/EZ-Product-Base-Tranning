l=list(map(int,input().split(" ")))
print("original list:",l)
def quick_sort(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left=[i for i in  l[1:] if  i<pivot ]
    print(left)
    right=[i for i in  l[1:] if  i>pivot]
    print(right)
    return quick_sort(left)+[pivot]+quick_sort(right)
res=quick_sort(l)
print("sorted array",res)

    

