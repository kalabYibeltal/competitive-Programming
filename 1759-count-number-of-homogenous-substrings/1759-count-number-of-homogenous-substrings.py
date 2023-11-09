class Solution:
    def countHomogenous(self, s: str) -> int:
        total = 0
        count = 1
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                total += count * ((count+1)/2)
                count  = 1
            else: count += 1
        
        return int(total + (count * ((count+1)/2))) % 1000000007
            