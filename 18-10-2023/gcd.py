m=0
n=4
'''ans=1
for i in range(2,n+1):
    if m%i==0 and n%i==0:
        ans=i
print(ans)'''
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1     
print(c)
