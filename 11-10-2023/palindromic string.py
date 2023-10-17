s=input()
#tar=int(input())

#brute force 
'''sub=[]
for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub.append(s[i:j])
print(sub)

def palindromic_string(s):
    max1=-1000
    min1=9999
    c=0
    for i in range(len(sub)):
        s=sub[i]
        if s==s[::-1]:
            c+=1
            print(s)
            if (len(s))>max1:
                max1=len(s)
                p=s
            if len(s)<min1 and len(s)!=1:
                min1=len(s)
                k=s
    return c,max1,p,min1,k


print(palindromic_string(sub))'''

