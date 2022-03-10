class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        i=0
        x="" 
        m=True
        if len(palindrome)==1:
            return x
        while i < len(palindrome):
            if palindrome[i] =='a':
                x =  x + palindrome[i]
            elif m:
                x =  x +'a'
                m=False
            else:
                x =  x + palindrome[i]
            i+=1
        y=""
        i=0
        left=0
        right=len(x)-1
        boll=True
        while left<=right:
            if x[left]!=x[right]:
                boll=False
                break
            left+=1
            right-=1
     
            
        if m or boll:
            while i < len(palindrome):
                if i==len(palindrome)-1:
                    y=y+'b'
                    break
                y=y+palindrome[i]
                
                i+=1
            return y
        return x
        
