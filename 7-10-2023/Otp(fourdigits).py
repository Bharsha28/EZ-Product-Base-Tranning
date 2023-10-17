n=input()
l=''
for i in range(1,len(n),2):
        l+=str(int(n[i])**2)
print(l[:4])