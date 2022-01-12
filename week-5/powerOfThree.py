class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n!=int(n):
            return False
        elif n==0:
            return False
        elif n==1:
            return True
        else:
            return self.isPowerOfThree(n/3)
