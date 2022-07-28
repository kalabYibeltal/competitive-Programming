class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        f = True
        summ = 0
        ans = inf
        while l < len(nums):
            if f and r < len(nums):
                # if not(r<len(nums)):
                summ += nums[r]
                if summ >= target:
                    f = False
                    ans = min(ans, r-l+1)
                    if ans == 1: return 1
                    print(summ)
                r += 1
            
            if not f:
                summ -= nums[l]
                if summ < target:
                    # print(summ)
                    if r == len(nums): break
                    f = True
                    
                else:
                    ans = min(ans,r-(l+1))
                    print(summ)
                    if ans == 1: return 1
                   
                l += 1
        
            elif r >= len(nums): break
                
        # print(r,l)
        if ans == inf: return 0
        return ans
