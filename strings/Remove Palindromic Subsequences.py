class Solution:
    def removePalindromeSub(self, s: str) -> int:
        p = False
        # s = "abba"
        
        if len(s) % 2 == 0:
            x = s[int(len(s)/2):int(len(s))]
            if s[0:int(len(s)/2)] == x[::-1]: return 1
            
        else:
            x = s[int(len(s)/2)+1:int(len(s))]
            if s[0:int(len(s)/2)] == x[::-1]: return 1
        
        return 2
    
    
    
        
