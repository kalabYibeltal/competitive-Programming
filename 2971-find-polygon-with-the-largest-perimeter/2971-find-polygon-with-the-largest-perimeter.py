class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        pre = [0]
        nums.sort()
        for n in nums:
            pre.append(pre[-1] + n)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < pre[i]:
                return pre[i+1]
            if i <= 2:
                return -1