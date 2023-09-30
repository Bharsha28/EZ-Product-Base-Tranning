def generate_list(n):
    l=[]
    for i in range(n):
        l1=[]
        for i in range(n):
            l1.append(i)
  jjj      l.append(l1)
    return l
print(generate_list(10))