'''
        1         
      1   2       
    1       3     
  1           4   
1   2   3   4   5
'''
n=5
start=n-1
end=n-1
var=2
flag=0
for i in range(n):
    for j in range(2*n-1):
        if j==start:
            print("1",end=" ")
        elif j==end:
            print(var,end=" ")
            var+=1
        elif i==n-1:
            val=2
            for k in range(1,2*n):
                if k%2==0:
                   print(val,end=" ")
                   val+=1
                else:
                   print(" ",end=" ")
            flag=1
            break
        else:
            print(" ",end=" ")
    if flag==1:
        break
    print()
    start-=1
    end+=1