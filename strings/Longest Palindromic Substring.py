class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxt = ""
        for i in range(len(s)):
            j = 1
            count = s[i]
            while i-j >= 0 and i+j < len(s):
                if s[i-j] == s[i+j]:
                    count = s[i-j] + count + s[i+j]
                else: break
                j += 1
            if len(count) > len(maxt): maxt = count
            
        for i in range(len(s)-1):
            j = 1
            if s[i] != s[i+1]: continue
            count = s[i] + s[i+1]
            while i-j >= 0 and i+1+j < len(s):
                if s[i-j] == s[i+1+j]:
                    count = s[i-j] + count + s[i+1+j]
                else: break
                j += 1
            print(count)
            if len(count) > len(maxt): maxt = count
                
        
        return maxt
