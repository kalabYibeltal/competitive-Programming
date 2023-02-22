class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)
        
        if '0' not in s:
            return 0
        c = 0
        while '01' in s:
            s = s.replace('01', '10')
            c += 1
        return c