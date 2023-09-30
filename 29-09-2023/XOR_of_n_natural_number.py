n=int(input())
val=0
for i in range(1,n+1):
    val=val^i
print("XOR values from 1 to ",n,"is:",val)

#optimize
if(n%4==0):
    print(n)
elif(n%4==1):
    print(1)
elif(n%4==2):
    print(n+1)
elif(n%4==3):
    print(0)