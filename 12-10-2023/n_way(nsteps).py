n=int(input())
def find_way(n):
    if n==1:
        return 1
    if n<=0:
        return 0
    return find_way(n-1)+find_way(n-2)+find_way(n-3)
print(find_way(n))

def fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fib(n-1)+fib(n-2)
s=0
for i in range(n):
    s+=fib(i)
print(s)