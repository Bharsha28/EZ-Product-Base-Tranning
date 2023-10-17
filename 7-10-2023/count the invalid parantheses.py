##Check wether the given string of paranthesis is balanced or not with function
def valid_paranthesis(s):
    stack=[]
    n=len(s)
    flag=1
    i=0
    while i<n:
        if s[i]=='(' or s[i]=='{' or s[i]=='[':
            stack.append(s[i])
        elif s[i]==')' or s[i]=='}' or s[i]==']':
            if not stack:
                flag=0
                return i+1
                break
            elif (s[i]==')' and stack[-1]=='(') or (s[i]=='}' and stack[-1]=='{') or (s[i]==']' and stack[-1]=='['):
                stack.pop()
            else:
                flag=0
                return i+1
        else:
            flag=0
            return i+1
            break
        i+=1
    if flag!=0 and not stack:
        return 0
    if flag==1:
        return i+1
s=input()
print(valid_paranthesis(s))
'''s=input()
stack=[]
c=0
for i in s:
        if i=='[' or i=='{' or i=='(':
            stack.append(i)
            c+=1
        else:
            if (i=='}' and stack[-1]=='{') or( i==')' and stack[-1]=='(' ) or( i==']' and stack[-1]=='[' ):
                stack.pop()    
                c+=1
if  len(stack)==0:
    print(0)
elif c>=1 or len(stack)!=0 :
    print(c+1)
    print(" not balanced")'''