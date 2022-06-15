class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = 0
        ans = []
        for i in nums:
            prefix += i
            ans.append(prefix)
        
        return ans
            
