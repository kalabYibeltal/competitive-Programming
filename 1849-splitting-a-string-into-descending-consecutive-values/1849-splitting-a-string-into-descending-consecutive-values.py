class Solution:
    def splitString(self, s: str) -> bool:
          
        nott = int(s)
        def back(i,parent):
            if i == len(s):
                if parent == nott:
                    return False
                return True
            val = 0
            booll = False
            for index in range(i,len(s)):
                val = val*10 + int(s[index])
                if val == parent - 1 or parent == -1:
                    booll = booll or back(index + 1, val)
            
            return booll
        
        return back(0,-1)