n=int(input())
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
def sum1(n):
    if n==0:
        return 0
    else:
        return sum1(n)+sum1(n-1)
print(sum1(n))