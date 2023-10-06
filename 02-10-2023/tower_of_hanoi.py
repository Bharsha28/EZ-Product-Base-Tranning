def TOH(n, src, aux, dest):
    if n == 1:
        print("I moved from "+src+" to " + dest)
        return
    TOH( n-1, src, dest, aux)
    print("I moved from "+src+" to " + dest)
    TOH( n-1, aux, src, dest)
n = int(input())
TOH(n, 'src', 'aux', 'dest')
#to caluculate no.of moves
def toh(n):
    if(n==1):
        return 1
    else:
        return 2*toh(n-1)+1
n=int(input())
res=toh(n)
print(res)
