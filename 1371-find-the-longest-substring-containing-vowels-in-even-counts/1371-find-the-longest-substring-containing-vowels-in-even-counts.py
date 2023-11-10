class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        arr= [0,0,0,0,0]
        seen = {}
        seen[tuple(arr)] =  -1
        vowels = {'a':0 ,'e':1,'i':2,'o':3,'u':4}
    
        ans = 0
        
        for i in range(len(s)):
            l = s[i]
            
            if l in vowels:
                arr[vowels[l]] = 1 - arr[vowels[l]]
            
            if tuple(arr) not in seen:
                seen[tuple(arr)] = i
            
            ans = max(ans, i - seen[tuple(arr)])
        
        
        return ans
        