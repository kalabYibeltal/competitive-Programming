class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return 
        have = {}
        dictr = {}
        need = {}
        for c in s1:
            need[c] = 1 + need.get(c,0)
            have[c] = 0
            dictr[c] = 0
     
        
        # print(tr)
        left = right = 0
        while (right - left) < len(s1) and right < len(s2):
            if s2[right] in need:
                print(left,right)
                have[s2[right]] += 1
                print(have)
                if have[s2[right]] == need[s2[right]] and (right - left + 1) == len(s1): return True
                elif  have[s2[right]] <= need[s2[right]] and (right - left + 1) < len(s1): 3 * 5
                else:
                    while True:
                        have[s2[left]] -= 1
                        if s2[left] == s2[right]:
                            left = left + 1
                            break
                        left += 1
                                 
                
            else: 
                left = right + 1
                # print(dictr)
                have = dictr
                for c in dictr:
                    have[c] = 0
                # print(dictr)
                print(right,have,dictr)
            right += 1
        
        print(right,left)
        return False
                
        
        
