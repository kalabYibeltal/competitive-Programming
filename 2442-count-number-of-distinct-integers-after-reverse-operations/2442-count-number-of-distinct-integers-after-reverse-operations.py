class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set(nums)
        ans.update([int(str(x)[::-1]) for x in nums])
        return len(ans)