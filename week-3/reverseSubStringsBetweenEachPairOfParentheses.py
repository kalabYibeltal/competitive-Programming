class Solution:
    def reverseParentheses(self, s: str) -> str:
        i=0
        ptr=0
        strr=""
        strn=""
        n=len(s)
        while i<n:
            if s[i]=="(":
                ptr=i
                i+=1
            elif s[i]==")":
                strr=s[ptr+1:i]
                stro=strr[::-1]
                n=len(s)
                print(s)
                s=s[0:ptr]+stro+s[i+1:n]
                print(s)
                n=len(s)
                i=0
            else:
                i+=1
        return s
                
                
