class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s = bin(n)[2:]
        if n == 0: return False
        for c in range(1,len(s)):
            # print(s[c])
            if int(s[c]) == 1: return False
        
        return True
