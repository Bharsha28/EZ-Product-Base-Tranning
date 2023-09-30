n=int(input())
m=n
a=n
s=0
c=0
while(n>0):
    r=n%10
    s+=r
    n=n//10
print(s)
sum1=0
while(a>0):
    r=a%10
    a=a//10
    c+=1
for i in range(c):
    i=m%10
    sum1=sum1+i
    m=m//10
print(sum1)
    
    