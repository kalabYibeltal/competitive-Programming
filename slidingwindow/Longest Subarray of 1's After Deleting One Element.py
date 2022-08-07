class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = 0
        k = 1
        ans = 0
        while r < len(nums):
            if k == 0 and nums[r] == 0:
                if nums[l] == 0: 
                    k = 1
                l += 1                
                
            elif nums[r] == 0:
                k -= 1
                r += 1
                # print(r,l,k)
                ans = max(ans,r-l-1 ) 
            elif nums[r] == 1:
                r += 1
                # print(r,l)
                ans = max(ans,r-l -1) 
        
        return ans
            
