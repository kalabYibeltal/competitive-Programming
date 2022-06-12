class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        dictr = {}
        score = 0
        l = r = 0
        while r < len(nums):
            ans=max(ans,score)
            if nums[r] in dictr and dictr[nums[r]] > 0:
        
                while True:
                    if nums[l] == nums[r]: 
                        dictr[nums[l]] -= 1
                        score -= nums[l]
                        l += 1
                        break
                    dictr[nums[l]] -= 1
                    score -= nums[l]
                    l += 1
                    
            dictr[nums[r]] = 1 + dictr.get(nums[r],0)
            score += nums[r]
            r += 1
            
        # print(ans,score)
        ans=max(ans,score)
        return ans
