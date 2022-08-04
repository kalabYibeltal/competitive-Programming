class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        val = 0
        for i in nums:
            val = val ^ i
        
        arr = []
        h = pow(2,maximumBit) - 1
        for i in range(1,len(nums)+1):
            arr.append(h ^ val)
            val = val ^ nums[-i]
        
        return arr
