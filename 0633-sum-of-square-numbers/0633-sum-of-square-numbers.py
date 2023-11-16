class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        for i in range(c + 1):
            if i*i > c:
                return False
            if int(pow(c- i*i, 0.5)) == pow(c- i*i, 0.5):
                return True
            