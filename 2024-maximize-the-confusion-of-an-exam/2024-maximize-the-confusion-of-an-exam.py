class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        a = k
        l = 0
        r = 0
        m = 0
        answerkey = answerKey
        while r < len(answerkey):
            if a == 0 and answerkey[r] == "F":
                if answerkey[l] == "F":
                    print(r)
                    a += 1
                l += 1
            elif answerkey[r] == "T":
                r += 1
            else:
                a -= 1
                r += 1
            m = max(m,r-l)
        
        l = r = 0
        a = k
        while r < len(answerkey):
            if a == 0 and answerkey[r] == "T":
                if answerkey[l] == "T":
                    a += 1
                l += 1
            elif answerkey[r] == "F":
                r += 1
            else:
                a -= 1
                r += 1
            m = max(m,r-l)
        
        return m
            