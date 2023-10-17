n=int(input())
'''*
   **
   ***'''
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()
char=97
for i in range(n+1):
    for j in range(i):
        print(chr(char),end=" ")
        if char==122:
            char=97
        char+=1
    print()
s=n-1
e=n-1
mid=s
for i in range(n):
    for j in range(2*n-1):
        if j>=s and j<=mid:
            print("* ",end="")
        else:
            print(" ",end="")
    s-=1
    e+=1
    print()
