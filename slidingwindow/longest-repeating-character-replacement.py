class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        dictr = {}
        for i in s:
            if i in dictr: dictr[i] = 1
            else: dictr[i] = 1
        
        length = 0
        for i in dictr:
            l = r = 0
            val = k
            wid = 0
            while r < len(s):
                if s[r] == i:
                    wid += 1
                    r += 1
                elif val > 0:
                    val -= 1
                    r += 1
                    wid += 1
                elif s[l] == i:
                    l += 1
                    wid -= 1
                else:
                    l += 1
                    wid -= 1
                    val += 1
                
                length = max(wid, length)
            
        return length
                    
