def par(l):
    if len(l)==1:
        print("return",[l])
        return [l]
    ans=[]
    for i in range(len(l)):
        temp=[l[i]]
        print("i",i)
        print("temp",temp)
        sub=l[0:i]+l[i+1:]
        print(sub)
        parr=par(sub)
        #iprint(parr)
        for i in parr:
            ans.append(temp+i)
    return ans
l=[1,2]
print(par(l))
    