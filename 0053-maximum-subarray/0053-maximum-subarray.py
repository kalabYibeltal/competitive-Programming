class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [0]*(len(nums)+1)
        ans = -inf
        for i in range(len(nums)-1,-1,-1):
            arr[i] = max(arr[i+1]+nums[i], nums[i])
            ans = max(arr[i],ans)
        return ans
        