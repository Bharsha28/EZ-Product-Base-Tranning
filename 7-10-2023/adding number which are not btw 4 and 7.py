# input=2,5,1,4,3,2,7,8
# output=4343(2+5+1+8=16,4327,16+4327)
l=list(map(str,input().split(",")))
s=''
n=0
n1=l.index('4')
n2=l.index('7')
for i in range(0,n1):
    n+=int(l[i])
for i in range(n2+1,len(l)):
    n+=int(l[i])
s+=str(n)
st=""
l2=[]
for i in range(n1,n2+1):
    l2.append(str(l[i]))
for i in l2:
    st+=i
print(int(s)+int(st))