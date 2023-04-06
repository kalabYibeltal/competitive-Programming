class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # heap = []
        # for i in range(len(nums)):
        #     heappush(heap,[-nums[i],])
        Max = nums[0]
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            Max = max(Max, ceil(tot/(i+1)))
        
        return Max
        
        