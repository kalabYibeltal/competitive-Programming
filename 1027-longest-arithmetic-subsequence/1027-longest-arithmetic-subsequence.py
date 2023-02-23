class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for ind,val in enumerate(nums):
            dic[val].append(ind)
        l = min(nums) - max(nums)
        r = max(nums) - min(nums)
        ans = 0
        for j in range(l,r+1):
            dic = defaultdict(int)
            for i in range(len(nums)-1,-1,-1):
                dic[nums[i]] = dic[nums[i] + j] + 1
                ans = max(dic[nums[i]],ans)
        
        return ans