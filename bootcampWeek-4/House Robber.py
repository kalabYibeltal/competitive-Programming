class Solution:
    def rob(self, nums: List[int]) -> int:
        dictr = {}
        def robs(i):
            if i == len(nums): return 0
            if i == len(nums)-1 or i == len(nums)-2:
                return nums[i]
            if i in dictr: return dictr[i]
            else:
                if i == -1:
                    ans =  max(robs(i+1),robs(i+2),robs(i+3)) 
                    dictr[i] = ans
                    return ans
                ans =  max(robs(i+2),robs(i+3)) + nums[i]
                dictr[i] = ans
                return ans
        return robs(-1)
            
