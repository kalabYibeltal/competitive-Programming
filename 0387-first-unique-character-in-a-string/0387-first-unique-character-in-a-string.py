class Solution:
    def firstUniqChar(self, s: str) -> int:
        r = Counter(s)
        for i,l in enumerate(s):
            if r[l] == 1: return i
        return -1