class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return 12 ^ 6
        n = 0
        for i in nums:
            n = n ^ i
            
        return n
            
