class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictr = {}
        for i in nums:
            if i in dictr: return True
            dictr[i] = 1
        
