class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre = 0
        n = inf
        for i in nums:
            pre += i
            n = min(n,pre)
        
        return max(1,1 - n)
        
