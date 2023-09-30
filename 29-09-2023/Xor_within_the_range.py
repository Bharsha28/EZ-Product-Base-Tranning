n=int(input())
m=int(input())
xor=0
for i in range(n,m+1):
    xor=xor^i
print("XOR values from 1 to ",n,"is:",xor)
xor=0
xor=(xor^m)^(xor^(n-1))
print("XOR values from 1 to ",n,"is:",xor)