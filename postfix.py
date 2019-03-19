s='1 2 + 4 * 3 +'
s.split()
stack=[]
for i in range(len(s)):
    if s[i].isdigit():
        stack.append(s[i])
    elif s[i]=='+':
       l=int(stack.pop())
       k=int(stack.pop())
       m=k+l
       stack.append(m)
       
        
    elif s[i]=='-':
        l=int(stack.pop())
        k=int(stack.pop())
        m=k-l
        stack.append(m)
        
        
    elif s[i]=='*':
        l=int(stack.pop())
        k=int(stack.pop())
        m=k*l
        stack.append(m)
        
    elif s[i]=='%':
        l=int(stack.pop())
        k=int(stack.pop())
        m=k%l
        stack.append(m)
        
        
res=stack.pop()
print(res)
