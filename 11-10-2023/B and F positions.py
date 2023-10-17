s=input()
l=[0,]
c=0
for i in range(len(s)):
    if s[i]=='B' and i>0:
        c-=1
    elif s[i]=='F':
        c+=2
    if c not in l:
        l.append(c)
print(l)