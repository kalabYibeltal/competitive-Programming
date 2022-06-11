class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dictr = {2:3,5:6}
        # del dictr[2]
        # print(len(dictr))
        # return 
        leng = 0
        dictr = {}
        left = right = 0
        while right < len(s):
            if s[right] in dictr:
                if len(dictr) > leng: leng = len(dictr)
                dictr[s[right]] += 1
        
                while dictr[s[right]] != 1:
                    dictr[s[left]] -= 1
                    if dictr[s[left]] == 0: del dictr[s[left]]
                    left += 1
            else: dictr[s[right]] = 1
            # print(dictr)
            right += 1
        
        return max(leng,len(dictr))
        
