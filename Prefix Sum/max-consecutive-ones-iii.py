class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        a = k
        l = 0
        r = 0
        m = 0
        answerkey = nums
        while r < len(answerkey):
            if a == 0 and answerkey[r] == 0:
                if answerkey[l] == 0:
                    a += 1
                l += 1
            elif answerkey[r] == 1:
                r += 1
            else:
                a -= 1
                r += 1
            m = max(m,r-l)
        
        return m
