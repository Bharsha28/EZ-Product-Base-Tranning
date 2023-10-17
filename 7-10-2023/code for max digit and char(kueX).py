# input=abhishek:43848 Mayur:37491 Freind:3949 Yeah:7878
# output=kuiX
d=dict()
l=list(input().split())
for i in range(len(l)):
    name,code=l[i].split(":")
    d[name]=(code)
res=''
for key,val in d.items():
    n=len(key)
    mx=-1
    for i in range(len(val)):
        if mx<int(val[i]) and int(val[i])<=n and int(val[i])>0:
            mx=int(val[i])
    if mx==-1:
        res+='X'
    else:
        res+=key[mx-1]
print(res)