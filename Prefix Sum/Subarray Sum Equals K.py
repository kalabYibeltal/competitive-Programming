#got help from neetcode-youtube channel
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictr = {}
        ans = 0
        dictr[0]=1
        prefix = 0
        for i in nums:
            prefix += i
            if (prefix-k) in dictr:
                ans += dictr[prefix-k]
            if prefix in dictr: dictr[prefix] += 1
            else: dictr[prefix] = 1
        
        return ans
