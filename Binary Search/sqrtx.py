class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left < right - 1:
            mid = (left+right)//2
            if mid*mid == x: return mid
            elif mid * mid > x: right = mid - 1
            else: left = mid 
        
        if right * right <= x: return right
        return left
