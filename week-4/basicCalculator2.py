def calc(a:int,b:int,c: str) -> int:
    if c=="*":
        return a*b
    elif c=="/":
        return int(a/b)
    elif c=="-":
        return a-b
    else:
        return a+b
    
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        sd=[]
        i=0
        arr=""
        while i<len(s):
            if s[i]==" ":
                print(s[i])
                i+=1
                continue
            
            while i<len(s) and not(s[i]==" " or s[i]=="/" or s[i]=="*" or s[i]=="+" or s[i]=="-"):
                arr=arr+s[i]
                i+=1
            if not(arr==""):
                stack.append(int(arr))
            if i==len(s):
                break
            if not (s[i]==" "):
                stack.append(s[i])
            else:
                i=i-1
            arr=""
            i+=1
            
        stack.reverse()
        y=stack.pop()
        #print(len(stack))
        #print(stack)
        
        while len(stack)>0:
            if len(stack)==2:
                y=calc(y,stack[-2],stack[-1])
                stack.pop()
                stack.pop()
            elif stack[-1]=="*":
                y=calc(y,stack[-2],"*")
                stack.pop()
                stack.pop()
            elif stack[-1]=="/":
                y=calc(y,stack[-2],"/")
                stack.pop()
                stack.pop()
            else:
                if stack[-3]=="*":
                    x=calc(stack[-2],stack[-4],"*")
                    z=stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append(x)
                    stack.append(z)
                elif stack[-3]=="/":
                    x=calc(stack[-2],stack[-4],"/")
                    z=stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append(x)
                    stack.append(z)
                else:
                    y=calc(y,stack[-2],stack[-1])
                    stack.pop()
                    stack.pop() 
        return y
