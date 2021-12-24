class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i=0
        n=len(tokens)
        while i<n:
            if tokens[i]=="+":
                x=int(tokens[i-1])
                print(tokens[i-2])
                y=int(tokens[i-2])
                tokens[i-2]=x + y
                tokens.pop(i)
                tokens.pop(i-1)
                i=i-1
                n=n-2
            elif tokens[i]=="-":
                tokens[i-2]=int(tokens[i-2])-int(tokens[i-1])
                tokens.pop(i)
                tokens.pop(i-1)
                i=i-1
                n=n-2
            elif tokens[i]=="/":
                tokens[i-2]=int(int(tokens[i-2])/int(tokens[i-1]))
                tokens.pop(i)
                tokens.pop(i-1) 
                i=i-1
                n=n-2
            elif tokens[i]=="*":
                tokens[i-2]=int(tokens[i-2]) * int(tokens[i-1])
                tokens.pop(i)
                tokens.pop(i-1)
                i=i-1
                n=n-2
            else:
                i=i+1
        return tokens[-1]
