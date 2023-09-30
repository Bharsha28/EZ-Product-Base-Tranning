n=int(input("Enter number"))
k=int(input("Enter postion"))
m=n&(1<<(k-1))
if(m>=1):
    print("set bit")
else:
    print("not set bit")