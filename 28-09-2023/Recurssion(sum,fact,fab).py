n=int(input())
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print("fact",fact(n))
#fabinacioo
def fib(n):
    if(n==0 ):
        return 0
    elif( n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
print("fib",fib(n))    
def add(n):
    if(n<=0):
        return 0
    else:
       return n+add(n-1)
print("Add:",add(n)) 