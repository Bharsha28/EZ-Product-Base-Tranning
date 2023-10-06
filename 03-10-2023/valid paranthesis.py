s=input()
stack=[]
c=0
if len(s)%2!=0:
    print("not balanced")
else:    
    for i in s:
        if i=='[' or i=='{' or i=='(':
            stack.append(i)
        else:
            if (i=='}' and stack[-1]=='{') or( i==')' and stack[-1]=='(' ) or( i==']' and stack[-1]=='[' ):
                 stack.pop()    
            else:
                c+=1                     
    if  len(stack)==0:
        print("balanced")
    elif c>=1 or len(stack)!=0 :
        print("not balanced")