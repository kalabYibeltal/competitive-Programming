class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = 0
        s = 0
        l = r = 0
        while r < k:
            s += nums[r]
            r += 1
        avg = s/k
        
        while r < len(nums):
            s -= nums[l]
            s += nums[r]
            avg = max(avg,s/k)
            l += 1
            r += 1
        
        return avg
