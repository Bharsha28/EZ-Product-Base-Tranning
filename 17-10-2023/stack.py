l=[1,2,3,4,5,6]
l.append(7)
l.append(8)
print(l)
print(l.pop())
print(l.pop())
print("stack after pop",l)
if len(l)>=1:
    print("top of stack",l[-1])
else:
    print(l[0])
