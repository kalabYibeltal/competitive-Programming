class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        n = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
          
            for j in strs:
                if (i < len(j) and j[i] != c) or i >= len(j):
                    return n
            n += c
        return n
         
 
