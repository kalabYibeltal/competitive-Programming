class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        have = 0
        dictr = {}
        for i in range(0,len(t)):
            if t[i] in dictr: dictr[t[i]] += 0
            else: dictr[t[i]] = 0
       
        dictrt = {}
        need = 0
        for i in range(0,len(t)):
            if t[i] in dictrt: dictrt[t[i]] += 1
            else: 
                need += 1
                dictrt[t[i]] = 1
        
        left = right = 0
        res= [0,inf]

                       
        while right < len(s):
            if s[right] in dictr:
                dictr[s[right]] += 1
                if dictr[s[right]] == dictrt[s[right]]:
                    have += 1
                    
                    while have == need:
                        # print(left,right)
                        if right - left < res[1]- res[0]:
                            res = [left,right]
                        
                        if s[left] in dictr:
                            dictr[s[left]] -= 1
                            if dictr[s[left]] < dictrt[s[left]]:
                                have -= 1
                        left += 1
                       

            right += 1 
        
        if res[1] >100000000000: return ""
        return s[res[0]:res[1]+1]
                    
        
        
        
