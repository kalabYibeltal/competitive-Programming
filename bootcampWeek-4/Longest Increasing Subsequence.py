class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dictr = {}
        def length(i):
            if i in dictr: return dictr[i]
            maxx = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    count = length(j)
                    if count > maxx:
                        maxx = count
                        
            ans = maxx + 1
            dictr[i] = ans
            return ans
        
        # return length(0)
        maxcount = 0
        for k in range(0, len(nums)):
            x =  length(k)
            if x > maxcount: maxcount = x
        return maxcount
