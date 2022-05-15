class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        str=""
        if needle=="":
            return 0
        while((len(haystack)-i-len(needle)))>-1:
            if haystack[i]==needle[0]:
                str=haystack[i:i+len(needle)]
                if str==needle:
                    return i
            i=i+1
        return -1
